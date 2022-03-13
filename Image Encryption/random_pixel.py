import numpy as np
from PIL import Image
import random, json

png_file = ['zero.png', 'pp.jpg'][1]
img = Image.open(png_file)
I = np.asarray(img)

side = width, height = img.size
print(side) 

zero_json={}
for x in range(width):
    for y in range(height):
        r, g, b = I[y][x]
        zero_json.update({ f'{x},{y}' : f'{r},{g},{b}' })

# with open(png_file + '_.json', 'w') as fp:
#     json.dump(zero_json, fp) 

img = Image.open(png_file)
I = np.asarray(img)
side = width, height = img.size

# with open(png_file + '_.json', 'r') as js:
#     zero_json = js.read()
# zero_json = json.loads(zero_json)

vjs = zero_json.values()
kjs = zero_json.keys()
sort_vjs = list(vjs)

# ----------------------------

# from collections import deque
# sort_vjs = deque(sort_vjs)
# sort_vjs.rotate(len(vjs)//2)
# sort_vjs = list(sort_vjs)

# ----------------------------

# random.shuffle(sort_vjs)
sort_vjs.sort()

# -----------------------------

ones_json = dict(zip(kjs, sort_vjs))
data = np.ones((height, width, 3), dtype=np.uint8)

for x in range(height):
    for y in range(width):
        
#         val = zero_json[f'{y},{x}']
        val = ones_json[f'{y},{x}']
        data[x, y] = val.split(',')
        
#         rgb = r, g, b = I[x][y]
#         data[x, y] = rgb
        
img = Image.fromarray(data, 'RGB')
# img.save('edited.png')
img.save('random_' + png_file)

side = width, height = img.size
print(side)
