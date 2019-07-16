import yaml 
import os
from os import path

current_folder = path.dirname(__file__)

with open(path.join(current_folder, "config.yml"), "r") as stream:
    yamlconfig = yaml.full_load(stream)