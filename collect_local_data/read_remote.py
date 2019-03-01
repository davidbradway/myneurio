from __future__ import print_function
import sys
sys.path.append('..')
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
    # loop every second
    for i in range(60):
        print(i, end=' ')
        sys.stdout.flush()
        time.sleep(1)
    print('')
    try:
        my_list = nc.get_samples_live(user_info['locations'][0]['sensors'][0]['sensorId'])
    except:
        pass
    my_list.reverse()
    timestamp = [i['timestamp'] for i in my_list]
    p_W = [i['consumptionPower'] for i in my_list]
    data = {'timestamp': timestamp, 'p_W': p_W}
    return json.dumps(data)

if __name__ == '__main__':
    print(detect())
