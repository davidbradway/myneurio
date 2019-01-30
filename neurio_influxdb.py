from __future__ import print_function
from influxdb import InfluxDBClient
import my_keys
import neurio
import time
import json
import sys


# Setup authentication:
tp = neurio.TokenProvider(key=my_keys.key, secret=my_keys.secret)
# Create client that can authenticate itself:
nc = neurio.Client(token_provider=tp)
# Get user information (including sensor ID and location ID)
user_info = nc.get_user_information()

if __name__ == "__main__":
    try:
        print("Loop started")
        while(True):
            try:
                client = InfluxDBClient('localhost', 8086, 'admin', 'admin', 'hackaday')
                client.create_database('hackaday')
                sample = nc.get_local_current_sample(user_info['locations'][0]['sensors'][0]['ipAddress'])
                i = sample['channels'][2]['p_W']
                print(i)
                json_body = [
                    {
                        "measurement": "neurioData",
                        "tags": {
                            "source": "Ch2",
                            "type": "p_W"
                        },
                        "fields": {
                            "value": i
                        }
                    }
                ]
                client.write_points(json_body)
                #result = client.query('select value from sensorData;')
                #print("Result: {0}".format(result))
            except:
                pass
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("\n\nExiting")
