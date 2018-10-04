from __future__ import print_function
import neurio
import my_keys

# Setup authentication:
tp = neurio.TokenProvider(key=my_keys.key, secret=my_keys.secret)
# Create client that can authenticate itself:
nc = neurio.Client(token_provider=tp)
# Get user information (including sensor ID and location ID)
user_info = nc.get_user_information()

print("Sensor ID %s, location ID %s" %(user_info["locations"][0]["sensors"][0]["sensorId"],
  user_info["locations"][0]["id"]))

# Fetch sample:
sample = nc.get_samples_live_last(sensor_id=user_info["locations"][0]["sensors"][0]["sensorId"])

print("Current power consumption: %d W" % (sample['consumptionPower']))
