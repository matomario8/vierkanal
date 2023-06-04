import yaml

class Config:

    config: dict

    def _register_config(self, config_path):
        with open(config_path, "r") as config_file:
            self.config = yaml.safe_load(config_file)

    def __init__(self, config_path):
        self._register_config(config_path)
 
    def get(self):
        return self.config

    def get_db_host(self):
        return self.config["database"]["host"]

    def get_allowed_origins(self):
        return self.config["api"]["allowed_origins"]
