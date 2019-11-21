# coding=utf-8
import os
import argparse
import datetime,time
import tensorflow as tf
import numpy as np
from math import ceil
from  tensorflow.contrib.slim.python.slim.nets import inception_v3

slim = tf.contrib.slim

parser = argparse.ArgumentParser(description="Start a tensorflow model serving")
parser.add_argument('--model_path', dest="model_path", required=True)
parser.add_argument('--dataset_path', dest="dataset_path", required=True)
parser.add_argument('--label_path', dest="label_path", required=True)
parser.add_argument('--output_dir', dest="output_dir", required=True)
parser.add_argument('--batch_size', dest="batch_size", type=int, required=True)

args = parser.parse_args()

image_size = 299
num_channel = 3
num_partitions = 1
index = 0
if os.environ.get('OMPI_COMM_WORLD_RANK') is not None:
    index = int(os.environ.get('OMPI_COMM_WORLD_RANK'))
if os.environ.get('OMPI_COMM_WORLD_SIZE') is not None:
    num_partitions = int(os.environ.get('OMPI_COMM_WORLD_SIZE'))
if os.environ.get('OMPI_COMM_WORLD_LOCAL_RANK') is not None:
    os.environ['CUDA_VISIBLE_DEVICES'] = os.environ.get('OMPI_COMM_WORLD_LOCAL_RANK')


def get_class_label_dict(label_file):
  label = []
  proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label


class DataIterator:
    def __init__(self, data_dir):
        self.file_paths = []
        image_map = os.path.join(data_dir, "list.txt")
        if os.path.exists(image_map):
            with open(image_map) as f:
                image_list = f.readlines()  # Read the first line.
                total_size = len(image_list)
                partition_size = int(total_size / num_partitions)
                image_list = image_list[index * partition_size: min((index + 1) * partition_size, total_size) - 1]
                self.file_paths = [data_dir + '/' + file_name.rstrip() for file_name in image_list ]
                print("Worker {0} needs to process {1} images".format(str(index), str(len(image_list))))

        self.labels = [1 for file_name in self.file_paths]

    @property
    def size(self):
        return len(self.labels)

    def input_pipeline(self, batch_size):
        images_tensor = tf.convert_to_tensor(self.file_paths, dtype=tf.string)
        labels_tensor = tf.convert_to_tensor(self.labels, dtype=tf.int64)
        input_queue = tf.train.slice_input_producer([images_tensor, labels_tensor], shuffle=False)
        labels = input_queue[1]
        images_content = tf.read_file(input_queue[0])

        image_reader = tf.image.decode_jpeg(images_content, channels=num_channel, name="jpeg_reader")
        float_caster = tf.cast(image_reader, tf.float32)
        new_size = tf.constant([image_size, image_size], dtype=tf.int32)
        images = tf.image.resize_images(float_caster, new_size)
        images = tf.divide(tf.subtract(images, [0]), [255])

        image_batch, label_batch = tf.train.batch([images, labels], batch_size=batch_size, capacity=5 * batch_size)
        return image_batch


def main(_):
    start_time = datetime.datetime.now()
    label_dict = get_class_label_dict(args.label_path)
    classes_num = len(label_dict)
    test_feeder = DataIterator(data_dir=args.dataset_path)
    total_size = len(test_feeder.labels)
    count = 0
    with tf.Session() as sess:
        test_images = test_feeder.input_pipeline(batch_size=args.batch_size)
        with slim.arg_scope(inception_v3.inception_v3_arg_scope()):
            input_images = tf.placeholder(tf.float32, [args.batch_size, image_size, image_size, num_channel])
            logits, _ = inception_v3.inception_v3(input_images,
                                                        num_classes=classes_num,
                                                        is_training=False)
            probabilities = tf.argmax(logits, 1)

        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        saver = tf.train.Saver()
        saver.restore(sess, args.model_path)
        with open(args.output_dir +"/result-labels-{0}.txt".format(str(index)), "w") as result_file:
            i = 0
            while count < total_size and not coord.should_stop():
                test_images_batch = sess.run(test_images)
                file_names_batch = test_feeder.file_paths[i*args.batch_size: min(test_feeder.size, (i+1)*args.batch_size)]
                results = sess.run(probabilities, feed_dict={input_images: test_images_batch})
                new_add = min(args.batch_size, total_size-count)
                count += new_add
                i += 1
                for j in range(new_add):
                    result_file.write(os.path.basename(file_names_batch[j]) + ": " + label_dict[results[j]] + "\n")
                result_file.flush()
                print("Worker {0} Processed {1}/{2} images, took {3}".format(str(index), str(count), str(total_size),
                                                                             datetime.datetime.now() - start_time))

            coord.request_stop()
            coord.join(threads)


if __name__ == "__main__":
    tf.app.run()
