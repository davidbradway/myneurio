from __future__ import print_function
from influxdb import InfluxDBClient
import threading_timer_decorator_exit
import neurio
import time
import os

@threading_timer_decorator_exit.exit_after(5)
def slow_calls():
    sample = nc.get_local_current_sample(user_info['locations'][0]['sensors'][0]['ipAddress'])
    i = sample['channels'][2]['p_W']
    json_body = [{"measurement": "neurioData",
                  "tags": {
                   "source": "Ch2",
                   "type": "p_W"},
                  "fields": {"value": i}}]
    client.write_points(json_body)
    print("Wrote: {0}".format(i), flush=True)
    #result = client.query('select value from sensorData;')
    #print("Result: {0}".format(result))


if __name__ == "__main__":
    try:
        # Setup authentication:
        tp = neurio.TokenProvider(key=os.environ.get('NEURIO_KEY'), secret=os.environ.get('NEURIO_SECRET'))
        # Create client that can authenticate itself:
        nc = neurio.Client(token_provider=tp)
        # Get user information (including sensor ID and location ID)
        user_info = nc.get_user_information()

        #client = InfluxDBClient('localhost', 8086, 'admin', 'admin', 'hackaday')
        client = InfluxDBClient('influxdb', 8086, 'admin', 'admin', 'hackaday')
        client.create_database('hackaday')

        print("Loop started")
        while(True):
            try:
                slow_calls()
            except (KeyboardInterrupt, Exception) as error:
                print(error)
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("\n\nExiting")
