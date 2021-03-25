#! /usr/bin/env python3
 
import os 
import requests
import re 

descDir = 'supplier-data/descriptions/' 
imageDir = 'supplier-data/images/'

txtFiles = sorted(os.listdir(descDir))
jpegImages = sorted([image_name for image_name in os.listdir(image_path) if '.jpeg' in image_name])

listDir = []
imageCounter = 0

for file in txtFiles:
    key = ['name', 'weight', 'description']
    
    with open(descDir + file, 'r') as f:
        finalDicts = {}
        dicts = f.read().split("\n")[0:3]  

        dicts[1] = int((re.search(r'\d+', dicts[1])).group()) 

        descCounter = 0
        for dict in dicts:
            finalDicts[key[descCounter]] = dict
            descCounter += 1

        finalDicts['image_name'] = jpegImages[imageCounter]

        listDir.append(data)
        imageCounter += 1


for item in listDir:
    response = requests.post('http://35.184.213.186/fruits/', json=item)
    if response.status_code != 201: 
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))
