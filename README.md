# Azure AI Camp

Here, the ML practioner will learn how to use Azure ML, Databricks and other Microsoft AI technologies to unlock insights on big datasets and deploy AI services to the cloud and edge.  It is designed as a hands-on workshop experience, recommended in instructor-led format or on-demand learning by using the documentation and resources provided for guidance.

## Prerequisites

1.  Python proficiency
2.  Azure Storage Account
3.  Access to an Azure Databricks Workspace and pre-provisioned cluster of type: 
  - SKU: `Standard_D16_v3`
  - Runtime `6.1 ML (includes Apache Spark 2.4.4, Scala 2.11)`.
5.  Access to an Azure ML Workspace  - https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-manage-workspace

Please, also, ensure:

- Storage container in Azure Storage Account called "aicamp"
- Git installed locally
- Python 3 locally (Anaconda or Miniconda recommended)
- Code editor like VSCode (recommended) or PyCharm

## Agenda

### Day 1​
---
* (1)  AI at MS Overview​
    * (1.1) Cognitive Services overview
    * (1.2) Azure ML overview
    * _Break_
    * (1.3) Databricks with Azure ML overview
*  _Lunch_
* (2)  Auto ML with Databricks
* (3)  Azure ML with Databricks and Spark ML
*  _Break_
* (4) Parallel and distributed training​

​
### Day 2​
---

* (1) Azure ML on Data Science Virtual Machine
    * (1.1) Azure ML with AML Compute for Image Classification
    * _Break_
    * (1.2) Real world example in VSCode
*  _Lunch_
* (2) Deploy an Azure ML model as an Edge Module
*  _Break_
* (3) QnA Sessions
* _Break_
* (4) Wrap-up and feedback

## Technologies

1. Azure Databricks
2. Azure ML
3. Azure Storage
4. IoT Edge
5. Data Science Virtual Machine

## Repo structure

```
README.md
/day1
  /Readme.md
  notebooks
/day2
  /Readme.md
  notebooks
```

Setup on day-of
---

1. Git clone repo:  `git clone https://github.com/michhar/Azure-AI-Camp.git`
2. Set up an Azure Storage container
3. Download Azure ML Workspace `config.json`

### Addition links

#### Model Interpretability/Explainabilty:

https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-machine-learning-interpretability
 
#### AML Diagnostics:

https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-enable-app-insights

#### Cluster performance metrics can be analyzed and monitored using Ganglia.  This is documented at:

https://docs.microsoft.com/en-us/azure/databricks/clusters/clusters-manage#--monitor-performance

#### Intelligent Kiosk

https://github.com/microsoft/Cognitive-Samples-IntelligentKiosk
 
#### Uploading to blob

https://azure.microsoft.com/en-us/features/storage-explorer/

https://docs.microsoft.com/en-us/azure/data-factory/connector-azure-blob-storage

https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-cli

#### Upload a directory in Python:  

https://github.com/michhar/Azure-AI-Camp/tree/master/day2/1.1.ImageClassificationAmlCompute/scripts
 
#### Custom computer vision examples – reference implementations (new Microsoft OSS project)

https://github.com/microsoft/ComputerVision

#### OpenCV course: 

https://casis.llnl.gov/seminars/opencv

See OpenCV code examples in `Addition/`

#### "Horovod" and overall distributed training on Spark

Horovod Timeline slide example regarding how to measure the time of a worker is waiting for data in a MPI distributed scenario

`Addition/Distributed_Deep_Learning_Journey_(Horovod).pdf`

#### PetaStorm

A program that is often used with Horvod to build a distributed sampled dataset for DL:

https://docs.azuredatabricks.net/_static/notebooks/deep-learning/petastorm.html

#### Distributed processing

“Bandwidth optimal all-reduce algorithms for clusters of workstations. Journal of Parallel and Distributed Computing” :

http://websrv.cs.fsu.edu/~xyuan/paper/09jpdc.pd

#### Links on how AutoML feature selection and feature engineering works:

https://docs.microsoft.com/en-us/azure/machine-learning/service/concept-automated-ml

https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-create-portal-experiments#preprocess
 
 