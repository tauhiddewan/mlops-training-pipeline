# mlops-training-pipeline
ML-training-pipeline-demo This is a sample repository for creating training pipeline for ML model that will version control the dataset and model assets. This will also enable to reproduce the whole pipeline anywhere 

One time setup
```
dvc remote add -d ppline s3://<bucket-name>
dvc remote modify --local ppline access_key_id <your-access-key-id>
dvc remote modify --local ppline secret_access_key <secret-access-key> 
dvc repro 
```

if new data is added then push
```
dvc push
```

To reproduce, clone this repo and run the command
```
dvc repro
```
