#!/bin/sh
# executed from project root

python setup.py clean --all
python setup.py bdist_wheel --python-tag "$1"
