#!/bin/bash

cd ui
source activate usure_env
jupyter notebook 

<<COMMENT
init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test
COMMENT
