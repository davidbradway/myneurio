# collect local data

- this flask server can be used to collect data using a local request to the Neurio device
- the data are saved to a JSON file with a filename that includes a timestamp and the provided label
- these data are planned to be used to train a machine learning neural network mmodel
- the goal is to better detect events of interest such as when laundry starts, etc.
- note that there are a lot of hardcoded variables in here.

## Quick start

Get devloper keys to the Neurio API and fill out `my_keys.py`.
Fix the constants inside the for loop of `read_local.py` for your setup.
Use an environment (Conda, VirtualEnv, or Docker) described in parent directory as well.

`export FLASK_APP=app.py`

`flask run --host=0.0.0.0`

## Docker deployment

### without docker-compose

`docker build -t myn .`  
`docker run -d --name myncon -p 5000:5000 -v ./data:/app/data -e FLASK_APP=app.py myn`

## with docker-compose

`docker-compose up -d`
