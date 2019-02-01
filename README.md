# MYNEURIO

## Docs

http://api-docs.neur.io

## Setup

### With Conda

`conda env create -f environment.yml`  
`(source) activate myneurio`  
`(source) deactivate`  

### With venv and pip

`python3 -m venv .venv`  
`source .venv/bin/activate`  
`pip install -r requirements.txt`  
`deactivate`

## Manually edit your `my_keys.py` file to add your keys and credentials and do not add those secrets to the repo!

`git update-index --assume-unchanged my_keys.py`

## Usage

`cd example_neurio_scripts && python example_remote_api.py`  
`cd collectLabeledData && python read_local.py`  

## Flask

`cd collect_local_data`  
`export FLASK_APP=app.py`  
`flask run --host=0.0.0.0`  
`http://192.168.1.[PIIP]:5000/[LABEL]`
