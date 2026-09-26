import configparser
from pathlib import Path


class ConfigReader:

    def __init__(self):
        self.project_root = Path(__file__).resolve().parent.parent
        self.config_path = self.project_root / "config" / "config.ini"

        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

    def get(self, section, key):
        return self.config.get(section, key)

    def get_int(self, section, key):
        return self.config.getint(section, key)

    def get_boolean(self, section, key):
        return self.config.getboolean(section, key)