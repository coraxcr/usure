#!/bin/bash

cd ..

source activate usure_env

python -m usure.preprocessing.app

python -m usure.wordvectors.app


<<COMMENT

jupyter notebook 

init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test
COMMENT
