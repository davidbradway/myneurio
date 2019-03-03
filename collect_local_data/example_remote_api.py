from __future__ import print_function
import neurio
import os

# Setup authentication:
tp = neurio.TokenProvider(key=os.environ.get('NEURIO_KEY'), secret=os.environ.get('NEURIO_SECRET'))
# Create client that can authenticate itself:
nc = neurio.Client(token_provider=tp)
# Get user information (including sensor ID and location ID)
user_info = nc.get_user_information()

print("Sensor ID %s, location ID %s" %(user_info["locations"][0]["sensors"][0]["sensorId"],
  user_info["locations"][0]["id"]))

# Fetch sample from the remote API (not the local device.):
sample = nc.get_samples_live_last(sensor_id=user_info["locations"][0]["sensors"][0]["sensorId"])

print("Current power consumption: %d W" % (sample['consumptionPower']))
