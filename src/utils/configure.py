import yaml
import os

class Configure:
    # Configuration file in dictionary format
    _cfg:dict = None

    def __init__(self, filename:str = "config.yaml"):
        self._cfg = self.read(filename)

    # Get the value of a key in the configuration file
    def get(self, key: str) -> str:
        try:
            return self._cfg[key]
        except KeyError:
            print("Key not found in config file")
            return None

        
    # Read the configuration file
    def read(self, filename) -> dict:
        with open(filename, 'r') as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        # Set the environment variables
        if(config is None):
            return None
        return config

    def write_template(self):
        # Write a template configuration file
        with open("config_template.yaml", 'w') as file:
            for key in self._cfg.keys():
                yaml.dump({key: "Your " + key}, file)

cfg = Configure()
cfg.write_template()

