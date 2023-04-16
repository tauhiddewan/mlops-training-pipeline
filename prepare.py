
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path
import gdown
from utils import *
confs = get_configs()
np.random.seed(confs["RANDOM_SEED"])

def create_dataset():
    check_or_create_folders
    if download_path.exists()==False:
        gdown.download(confs["data_url"], str(download_path))
    df = pd.read_csv(download_path)
    df_train, df_test = train_test_split(df, random_state=confs["RANDOM_SEED"], test_size=.2)
    df_train.to_csv(str(dataset_path/"train.csv"), index=None)
    df_test.to_csv(str(dataset_path/"test.csv"), index=None)

create_dataset()

