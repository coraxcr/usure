"""Module for infrastructure configuration"""
from os import path
import yaml


class Config:
    """Configuration file"""

    def __init__(self):

        self._config_file = "config.yml"

        self._current_folder = path.dirname(__file__)

        self._loadvariables()


    def _get_full_path(self, path_part):
        """Join current folder path with other part."""
        return path.join(self._current_folder, path_part)


    def _loadvariables(self):
        """Load constants"""

        with open(path.join(self._current_folder, self._config_file), "r") as stream:

            self._yamlconfig = yaml.full_load(stream)

        self._filesystem = self._yamlconfig["persistence"]["file_system"]

        self.unpreprocessed = self._get_full_path(self._filesystem["unpreprocessed"])

        self.preprocessed = self._get_full_path(self._filesystem["preprocessed"])

        self.embeddings = self._get_full_path(self._filesystem["embeddings"])

        self.classification = self._get_full_path(self._filesystem["classification"])

        self.logs = self._get_full_path(self._filesystem["logs"])

        self.assets = self._get_full_path(self._filesystem["assets"])


    def set_to_test_mode(self):
        """Change load variables to test mode"""

        self._config_file = "config.test.yml"

        self._loadvariables()

config = Config()
config.set_to_test_mode()