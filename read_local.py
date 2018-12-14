from __future__ import print_function
#from gpiozero import Button
#from signal import pause
import my_keys
import neurio
import time
import json
import sys

#button = Button(18)
#button.when_pressed = detect

# Setup authentication:
tp = neurio.TokenProvider(key=my_keys.key, secret=my_keys.secret)
# Create client that can authenticate itself:
nc = neurio.Client(token_provider=tp)
# Get user information (including sensor ID and location ID)
user_info = nc.get_user_information()

timestamp = list()
p_W = list()

def detect():
    # while loop every second
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
    print(json.dumps({'timestamp': timestamp, 'p_W': p_W}, sort_keys=True, indent=4))
    data = json.dumps({'timestamp': timestamp, 'p_W': p_W})
    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)
#pause()
detect()
