#!/bin/bash

rm -rf ./dist

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine


python3 -m build


#推送之前需要 ~/.pypirc 中已经提前存放好token了
python3 -m twine upload ./dist/*