#!/bin/sh
# executed from project root

py_version="$1"
app_version=$(grep -oP "version='\K([\w\W]*)'" ./setup.py)
app_version=${app_version:: -1}

./scripts/build.sh "$py_version"
pip install --upgrade --no-cache ./dist/unidown_mr_de-"$app_version"-"$py_version"-none-any.whl[dev]
