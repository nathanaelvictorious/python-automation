#!/usr/bin/env python3

import os
from PIL import Image

dir = "supplier-data/images/"
images = os.listdir(dir)

for file in images :
  path, filename = os.path.split(file)

  if  (filename != "LICENSE" and filename != "README") :
    name, ext = filename.split('.')
    im = Image.open(dir+"/"+file).convert('RGB')

    im.resize((600,400)).save('supplier-data/images/{}.jpeg'.format(name))

  else :
    continue
    
print("Image Updated")
