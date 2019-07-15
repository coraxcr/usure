import yaml 
import os
from os import path

current_folder = path.dirname(__file__)

with open(path.join(current_folder, "config.yml"), "r") as stream:
    config = yaml.full_load(stream)

_corpora_path = config["persistence"]["file_system"]["corpora"] 

raw_corpora_folder_path = path.join(os.getcwd(), _corpora_path["raw"])
preprocessed_corpora_folder_path = path.join(os.getcwd(), _corpora_path["preprocessed"])
log_path = config["persistence"]["file_system"]["log"]