#! /usr/bin/env python3

import os
import requests

directory = "/data/feedback/"
url = "http://35.223.192.123/feedback/"

fullFeedback = {}
key = ["title", "name", "date", "feedback"]


for file in os.listdir(directory) :
  with open (dir+"/"+file, 'r') as text :
    i = 0

    for line in text :
      fullFeedback[key[i]] = line.rstrip('\n')
      i += 1

response = requests.post(url, json = fullFeedback)
