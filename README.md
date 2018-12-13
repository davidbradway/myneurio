# MYNEURIO

## Docs

http://api-docs.neur.io

## Setup

### With Conda

`conda env create -f environment.yml`  
`conda activate myneurio`

### With venv and pip

`python3 -m venv .venv`  
`source .venv/bin/activate`  
`pip install -r requirements.txt`  
`...`  
`deactivate`

## Manually edit your `my_keys.py` file to add your keys and credentials and do not add those secrets to the repo!

`git update-index --assume-unchanged my_keys.py`

## Usage

`python example.py`  
`python read_local.py`

