import json
import pickle 
import pandas as pd 
from utils import features_path, models_path , metrics_path
from sklearn.metrics import mean_squared_error
X_test = pd.read_csv(str(features_path / "test_features.csv"))
y_test = pd.read_csv(str(features_path / "test_labels.csv"))

model = pickle.load(open(str(models_path / "model.pickle"), "rb"))

r_sqrd = model.score(X_test, y_test)

y_pred = model.predict(X_test)

rmse = mean_squared_error(y_pred=y_pred, y_true=y_test)

with(open(str(metrics_path / "result.json"), "w")) as outfile:
    json.dump(dict(r_squared=r_sqrd, rmse=rmse), outfile)