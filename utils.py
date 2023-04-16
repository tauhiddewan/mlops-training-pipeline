import yaml
from pathlib import Path
BASE_PATH = Path(__file__).resolve().parent

def get_configs():
    config_path = BASE_PATH / 'confs.yaml'
    with open(config_path) as f:
        confs = yaml.safe_load(f)
    return confs

def check_or_create_folders():
    download_path.parent.mkdir(parents=True, exist_ok=True)
    dataset_path.mkdir(parents=True, exist_ok=True)
    features_path.mkdir(parents=True, exist_ok=True)
    models_path.mkdir(parents=True, exist_ok=True)
    metrics_path.mkdir(parents=True, exist_ok=True)


cfg = get_configs()
download_path = BASE_PATH /cfg["base_folder"] /cfg["download_dir"]
dataset_path = BASE_PATH /cfg["base_folder"] /cfg["dataset_dir"]
features_path = BASE_PATH /cfg["base_folder"] /cfg["features_dir"]
models_path = BASE_PATH /cfg["base_folder"] /cfg["models_dir"]
metrics_path = BASE_PATH /cfg["base_folder"] /cfg["metrics_dir"]

check_or_create_folders()
