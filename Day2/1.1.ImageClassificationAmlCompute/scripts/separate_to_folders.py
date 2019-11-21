import os
import glob
import shutil
import random

os.makedirs('data/train/normal', exist_ok=True)
os.makedirs('data/val/normal', exist_ok=True)
os.makedirs('data/train/suspicious', exist_ok=True)
os.makedirs('data/val/suspicious', exist_ok=True)

imglookup = {}

with open('cctvFrames_train_labels.csv') as f:
    for line in f:
        linespl = line.rstrip().split(',')
        imglookup[linespl[0]] = linespl[1]

imgfiles = glob.glob('train-green-butterfly-3349/*.jpg')
print(len(imgfiles))

for imgf in imgfiles:
    randnum = random.choice(range(10))
    if imglookup[os.path.basename(imgf)] == '1':
        if randnum not in [0,1]:
            shutil.copyfile(imgf, 'data/train/suspicious/' + os.path.basename(imgf))
        else:
            shutil.copyfile(imgf, 'data/val/suspicious/' + os.path.basename(imgf))
    else:
        if randnum not in [0,1]:
            shutil.copyfile(imgf, 'data/train/normal/' + os.path.basename(imgf))
        else:
            shutil.copyfile(imgf, 'data/val/normal/' + os.path.basename(imgf))

if __name__ == "__main__":
    pass
