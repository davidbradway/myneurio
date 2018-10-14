from __future__ import print_function
import neurio
import my_keys
import time

# Setup authentication:
tp = neurio.TokenProvider(key=my_keys.key, secret=my_keys.secret)
# Create client that can authenticate itself:
nc = neurio.Client(token_provider=tp)
# Get user information (including sensor ID and location ID)
user_info = nc.get_user_information()

# while loop every second
try:
    while True:
        sample = nc.get_local_current_sample(user_info['locations'][0]['sensors'][0]['ipAddress'])
        print(sample['timestamp'])
        print(sample['channels'][2]['p_W'])
        time.sleep(1.0 - (time.time() % 1.0))
except KeyboardInterrupt:
    pass

