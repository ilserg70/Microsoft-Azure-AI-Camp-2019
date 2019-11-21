# BrainScript CNTK GPU

This example uses the MNIST dataset to demonstrate how to train a convolutional neural network (CNN) on an Azure Batch AI cluster of one node.

## Details

- For demonstration purposes, MNIST dataset and ConvNet_MNIST.cntk will be deployed at Azure File Share;
- Standard output of the job and the model will be stored on Azure File Share;
- MNIST dataset (http://yann.lecun.com/exdb/mnist/) has been preprocessed by usign install_mnist.py available [here](https://batchaisamples.blob.core.windows.net/samples/mnist_dataset.zip?st=2017-09-29T18%3A29%3A00Z&se=2099-12-31T08%3A00%3A00Z&sp=rl&sv=2016-05-31&sr=c&sig=PmhL%2BYnYAyNTZr1DM2JySvrI12e%2F4wZNIwCtf7TRI%2BM%3D).
- ConvNet_MNIST.cntk config file is available [here](./ConvNet_MNIST.cntk). 

## Instructions to Run Recipe

### Jupyter Notebook

You can find Jupyter Notebook for this recipe in [CNTK-GPU-BrainScript.ipynb](./CNTK-GPU-BrainScript.ipynb).

### Azure CLI 2.0

You can find Azure CLI instructions for this recipe in [cli-instructions.md](./cli-instructions.md).

## License Notice

Under construction...

## Help or Feedback
--------------------
If you have any problems or questions, you can reach the Batch AI team at [AzureBatchAITrainingPreview@service.microsoft.com](mailto:AzureBatchAITrainingPreview@service.microsoft.com) or you can create an issue on GitHub.

We also welcome your contributions of additional sample notebooks, scripts, or other examples of working with Batch AI.
