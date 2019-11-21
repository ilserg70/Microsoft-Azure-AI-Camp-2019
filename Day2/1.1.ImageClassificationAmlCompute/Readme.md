# Image Classification with Azure ML, PyTorch and AmlCompute

1.  Download the data for the AI Camp [Click here to download](https://michharaicampstore.blob.core.windows.net/cvcamp-public/suspicious_behavior.zip)
2.  Locally, `pip install azure-storage-blob==2.1.0`
3.  Set the following environment variables

```
STORAGE_ACCOUNT_NAME
STORAGE_CONTAINER_NAME_TRAINDATA
STORAGE_ACCOUNT_KEY
```

4.  Unzip the data and run the `scripts/upload_to_blob.py` with `--dir data`
