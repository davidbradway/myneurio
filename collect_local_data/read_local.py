from __future__ import print_function
import sys
import my_keys
import neurio
import time
import json

# Setup authentication:
tp = neurio.TokenProvider(key=my_keys.key, secret=my_keys.secret)
# Create client that can authenticate itself:
nc = neurio.Client(token_provider=tp)
# Get user information (including sensor ID and location ID)
user_info = nc.get_user_information()

def detect():
    timestamp = list()
    p_W = list()
    # loop every second
    try:
        for i in range(120):
            print(i, end=' ')
            sys.stdout.flush()
            sample = nc.get_local_current_sample(user_info['locations'][0]['sensors'][0]['ipAddress'])
            timestamp.append(sample['timestamp'])
            p_W.append(sample['channels'][2]['p_W'])
            time.sleep(1.0 - (time.time() % 1.0))
    except KeyboardInterrupt:
        return
    print('')
    data = {'timestamp': timestamp, 'p_W': p_W}
    return json.dumps(data)

if __name__ == '__main__':
    print(detect())
