#!/usr/bin/env python3

import os
import requests

dir = "supplier-data/images/"
url = "http://localhost/upload/"

for file in os.listdir(dir) :
  with open(dir+"/"+file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
