#!/usr/bin/env python
"""
Copyright 2015, 2016 Jordan Husney <jordan.husney@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys
sys.path.append("..")

import neurio
import my_keys

tp = neurio.TokenProvider(key=my_keys.key, secret=my_keys.secret)
nc = neurio.Client(token_provider=tp)

sample = nc.get_samples_live_last(sensor_id=my_keys.sensor_id)

print("Current power consumption: %d W" % (sample['consumptionPower']))

