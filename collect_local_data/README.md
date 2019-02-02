# collect local data

- this flask server can be used to collect data using a local request to the Neurio device
- the data are saved to a JSON file with a filename that includes a timestamp and the provided label
- these data are planned to be used to train a machine learning neural network mmodel
- the goal is to better detect events of interest such as when laundry starts, etc.
- note that there are a lot of hardcoded variables in here.

## usage

Get a keys to the Neurio API and fill out `my_keys.py` in the parent directory of this one.
Fix the constants inside the for loop of `read_local.py` for your setup.
Use environment (Conda or VirtualEnv) described in parent directory as well.

`./run_flask.sh`

