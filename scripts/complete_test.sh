# executed from project root

pip install --upgrade .
cd test-plugin
pip install --upgrade .
cd ..

python setup.py clean --all
python setup.py bdist_wheel

flake8 ./unidown
pylint --rcfile=setup.cfg ./unidown/ || true
pyroma .

python setup.py check -v -m -s
twine check dist/*

sphinx-build -b html -j auto -T -E -a ./doc/ ./build/doc/html/
sphinx-build -b linkcheck ./doc/ ./build/doc/linkcheck/
