@echo off
python -m pip install -r requirements.txt
robot -d results --include smoke tests\
