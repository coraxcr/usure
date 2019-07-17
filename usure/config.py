import yaml 
import os
from os import path


_config_file = "config.yml"

_current_folder = path.dirname(__file__)

def _get_full_path(path_part):

    return path.join(_current_folder, path_part)

def loadyaml():

    global _yamlconfig

    with open(path.join(_current_folder, _config_file), "r") as stream:

        _yamlconfig = yaml.full_load(stream)

def change():

    global _filesystem, unpreprocessed, preprocessed, embeddings, classification, logs, assets

    _filesystem = _yamlconfig["persistence"]["file_system"]

    unpreprocessed = _get_full_path(_filesystem["unpreprocessed"])

    preprocessed = _get_full_path(_filesystem["preprocessed"])

    embeddings = _get_full_path(_filesystem["embeddings"])

    classification = _get_full_path(_filesystem["classification"])

    logs = _get_full_path(_filesystem["logs"])

    assets = _get_full_path(_filesystem["assets"])

def set_to_test_mode():

    global _config_file

    _config_file = "config.test.yml"

    loadyaml()
    
    change()

loadyaml()

change()

set_to_test_mode()