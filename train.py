import pickle 
import yaml
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from utils import features_path, models_path, cfg

X_train = pd.read_csv(str(features_path / "train_features.csv"))
y_train = pd.read_csv(str(features_path / "train_labels.csv"))

params = yaml.safe_load(open("params.yaml"))["train"]
n_estimators = params["n_estimators"]
max_depth = params["max_depth"]

model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=cfg["RANDOM_SEED"])
model = model.fit(X=X_train, y=y_train)

pickle.dump(model, open(str(models_path / "model.pickle"), "wb"))