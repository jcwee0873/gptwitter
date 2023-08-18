import os
import re
import json
import yaml
from dotenv import load_dotenv
from gpt_witter.config.singleton import Singleton

CURR_PATH = os.path.dirname(__file__)
ENV_PATH = os.path.join(CURR_PATH, '../..', '.env')
ENV_PATH = os.path.abspath(ENV_PATH)

load_dotenv(ENV_PATH)

class Config(metaclass=Singleton):
    def __init__(self, config_path=None) -> None:
        if not config_path:
            config_path = os.path.join(CURR_PATH, '../..', 'config.yaml')
            config_path = os.path.abspath(config_path)

        with open(config_path, 'r') as f:
            config = yaml.load(f, yaml.FullLoader)
            self.config = config
            self.config.update({k.lower():v for k, v in config.items()})

        self.debug = str(config.get('DEBUG')) == "True"

        self.base_llm_model = config.get('BASE_LLM_MODEL', 'gpt-3.5-turbo')
        self.fast_llm_model = config.get('FAST_LLM_MODEL', 'gpt-3.5-turbo')
        self.base_max_length = config.get("BASE_MAX_LENGTH", 4000)
        self.fast_max_length = config.get("FAST_MAX_LENGTH", 4000)
        self.temperature = config.get('TEMPERATURE', 0.5)


    def __getitem__(self, __name: str):
        return self.config[__name]
    