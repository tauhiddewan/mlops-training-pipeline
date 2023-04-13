import gdown
import numpy as np 
import pandas as pd
from datetime import date
from pathlib import Path
from utils import *
confs = get_configs()
np.random.seed(confs["RANDOM_SEED"])

def extract_features(df: pd.DataFrame):
    return df[["num_lectures", "price", "content_duration"]]

check_or_create_folders()
train_df = pd.read_csv(str(dataset_path / "train.csv"))
test_df = pd.read_csv(str(dataset_path / "test.csv"))
train_features_df = extract_features(train_df)
test_features_df = extract_features(test_df)

train_features_df.to_csv(str(features_path / "train_features.csv"), index=True)
test_features_df.to_csv(str(features_path / "test_features.csv"), index=True)

train_df.num_subscribers.to_csv(str(features_path / "train_labels.csv"), index=True)
test_df.num_subscribers.to_csv(str(features_path / "test_labels.csv"), index=True)
