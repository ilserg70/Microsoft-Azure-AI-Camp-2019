Please follow [instructions](/documentation/using-azure-cli-20.md) to install Azure CLI 2.0 and configure it for using with Batch AI.

### Create a Resource Group

Create a resource group ```batchaitests``` (or choose your own resource name) which will be used for resources creations:

```sh
az group create -n batchaitests -l eastus
```

### Create a Storage Account

Create a storage account with an unique name in the same region where you are going to use Batch AI:

```sh
az storage account create -n <storage account name> --sku Standard_LRS -l eastus -g batchaitests
```

### Data Deployment

- Download and extract preprocessed MNIST Database from this [location](https://batchaisamples.blob.core.windows.net/samples/mnist_dataset.zip?st=2017-09-29T18%3A29%3A00Z&se=2099-12-31T08%3A00%3A00Z&sp=rl&sv=2016-05-31&sr=c&sig=PmhL%2BYnYAyNTZr1DM2JySvrI12e%2F4wZNIwCtf7TRI%2BM%3D) into the current folder.

For GNU/Linux users:

```sh
wget "https://batchaisamples.blob.core.windows.net/samples/mnist_dataset.zip?st=2017-09-29T18%3A29%3A00Z&se=2099-12-31T08%3A00%3A00Z&sp=rl&sv=2016-05-31&sr=c&sig=PmhL%2BYnYAyNTZr1DM2JySvrI12e%2F4wZNIwCtf7TRI%2BM%3D" -O mnist_dataset.zip
unzip -o mnist_dataset.zip
```

- Download ConvNet_MNIST.cntk config file into the current folder:

For GNU/Linux users:

```sh
wget "https://raw.githubusercontent.com/Azure/BatchAI/master/recipes/CNTK/CNTK-GPU-BrainScript/ConvNet_MNIST.cntk?token=AcZzrfNpH_TV0LwzeHO_iGt4Kuh04on8ks5Z4bFrwA%3D%3D" -O ConvNet_MNIST.cntk
```

- Create an Azure File Share with `nmist_database` and `cntk_sample` folders and upload MNIST database and BrainScript ConvNet_MNIST.cntk config file:

```sh
az storage share create --name batchaisample --account-name <storage account name>
az storage directory create --share-name batchaisample --name mnist_database
az storage file upload --share-name batchaisample --source Train-28x28_cntk_text.txt --path mnist_database
az storage file upload --share-name batchaisample --source Test-28x28_cntk_text.txt --path mnist_database
az storage directory create --share-name batchaisample --name cntk_samples
az storage file upload --share-name batchaisample --source ConvNet_MNIST.cntk --path cntk_samples
```

### Cluster

For this recipe we need one node GPU cluster (`min node = max node = 1`) of `Standard_NC6` size (one GPU) with standard Ubuntu LTS (`UbuntuLTS`) or Ubuntu DSVM (```UbuntuDSVM```) image and Azure File share `batchaisample` mounted at `$AZ_BATCHAI_MOUNT_ROOT/external`.

#### Cluster Creation Command

For GNU/Linux users:

```sh
az batchai cluster create -l eastus -g batchaitests --storage-account-name <storage account name> -n nc6 -s Standard_NC6 --min 1 --max 1 --afs-name batchaisample --afs-mount-path external -u $USER -k ~/.ssh/id_rsa.pub
```

For Windows users:

```sh
az batchai cluster create -l eastus -g batchaitests --storage-account-name <storage account name> -n nc6 -s Standard_NC6 --min 1 --max 1 --afs-name batchaisample --afs-mount-path external -u <user_name> -p <password>
```

### Job

The job creation parameters are in [job.json](./job.json):

- Two input directories with IDs `CONFIG` and `DATASET` to allow the job to find the sample config and MNIST Database via environment variables `$AZ_BATCHAI_INPUT_CONFIG` and `$AZ_BATCHAI_INPUT_DATASET`;
- stdOutErrPathPrefix specifies that the job should use file share for standard output and error streams;
- An output directory with ID `MODEL` to allow job to find the output directory for the model via `$AZ_BATCHAI_OUTPUT_MODEL` environment variable;
- node_count defining how many nodes will be used for the job execution;
- ```microsoft/cntk:2.1-gpu-python3.5-cuda8.0-cudnn6.0``` docker image will be used for job execution.

Note, you can remove docker image information to run the job directly on DSVM.

#### Job Creation Command

```sh
az batchai job create -l eastus -g batchaitests -n cntk -r nc6 -c job.json
```

Note, the job will start running when the cluster finished allocation and initialization of the node.

### Next Steps

Azure CLI 2.0 Batch AI specific [documentation](/documentation/using-azure-cli-20.md) contains detailed information on
how to manage your clusters and jobs.

[CLI Quickstart](https://docs.microsoft.com/en-us/azure/batch-ai/quickstart-cli) contains an end-to-end example of using
Azure CLI 2.0 for Batch AI cluster creation, job submission and checking job's execution results.