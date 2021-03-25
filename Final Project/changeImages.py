#!/usr/bin/env python3

import os
from PIL import Image

path = os.getcwd()
images = os.listdir(path)

for file in images :
  im = Image.open(file).convert('RGB')

  name, ext = os.path.split(file)
  name = os.path.splitext(ext)[0]

  im.rotate(90).resize((128,128)).save('/opt/icons/{}.jpeg'.format(name))

print("Succeed")
