import pickle 
import pandas as pd 
from sklearn.linear_model import LinearRegression
from utils import features_path, models_path

X_train = pd.read_csv(str(features_path / "train_features.csv"))
y_train = pd.read_csv(str(features_path / "train_labels.csv"))

model = LinearRegression()
model = model.fit(X=X_train, y=y_train)

pickle.dump(model, open(str(models_path / "model.pickle"), "wb"))