import yaml

class Config:

    CONFIG: dict

    def __init__(cls):
        cls.CONFIG = None

    def register_config(cls, config_path):
        with open(config_path, "r") as config_file:
            cls.CONFIG = yaml.safe_load(config_file)
        