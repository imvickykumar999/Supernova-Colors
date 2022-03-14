import numpy as np
from PIL import Image
import random, json

png_file = 'test.png'
img = Image.open(png_file)
I = np.asarray(img)

side = width, height = img.size
print(side) 

zero_json={}
for x in range(width):
    for y in range(height):
        r, g, b = I[y][x]
        zero_json.update({ f'{x},{y}' : f'{r},{g},{b}' })

img = Image.open(png_file)
I = np.asarray(img)
side = width, height = img.size

vjs = zero_json.values()
kjs = zero_json.keys()

sort_vjs = list(vjs)
sort_kjs = list(kjs)

# ----------------------------

# d = {v : i for i, v in enumerate(sort_vjs)}
# from pprint import pprint as p
# p(d)

# sort_vjs = sorted(sort_vjs, key=len)

# up = {}
# for i in range(len(sort_vjs)):
#     up.update({sort_vjs[i] : d[sort_vjs[i]]})

# print(d==up)

# -----------------------------

ones_json = dict(zip(sort_kjs, sort_vjs))
data = np.ones((height, width, 3), dtype=np.uint8)

for x in range(height):
    for y in range(width):
        val = ones_json[f'{y},{x}']
        data[x, y] = val.split(',')
        
img = Image.fromarray(data, 'RGB')
img.save('test.png')
print('Done')
