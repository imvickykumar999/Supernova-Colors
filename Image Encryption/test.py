import numpy as np
from PIL import Image
import random, json

png_file = ['test.png', 'pp.jpg'][0]
img = Image.open(png_file)
I = np.asarray(img)

side = width, height = img.size
print(side) 

zero_json={}
for x in range(width):
    for y in range(height):
        r, g, b = I[y][x]
        zero_json.update({ f'{x},{y}' : f'{r},{g},{b}' })

with open(png_file + '_.json', 'w') as fp:
    json.dump(zero_json, fp) 

img = Image.open(png_file)
I = np.asarray(img)
side = width, height = img.size

# with open(png_file + '_.json', 'r') as js:
#     test_json = js.read()
# test_json = json.loads(test_json)

vjs = zero_json.values()
kjs = zero_json.keys()

sort_vjs = list(vjs)
sort_kjs = list(kjs)

# ----------------------------

# from collections import deque
# sort_vjs = deque(sort_vjs)
# sort_vjs.rotate(len(vjs)//2)
# sort_vjs = list(sort_vjs)

# ----------------------------

class Solution:
   def solve(self, nums):
      length = len(nums)
      for i in range(0,length,4):
         if(i+2<length):
            nums[i], nums[i+2] = nums[i+2], nums[i]
         if(i+3<length):
            nums[i+1], nums[i+3] = nums[i+3], nums[i+1]
      return nums

ob = Solution()
sort_vjs = ob.solve(sort_vjs)

# test_vjs = list(test_json.values())
# test_vjs = ob.solve(test_vjs)
# print(sort_vjs == test_vjs)

# ----------------------------

random.shuffle(sort_vjs)
# sort_vjs.sort()
# sort_kjs.sort()

# -----------------------------

ones_json = dict(zip(sort_kjs, sort_vjs))
data = np.ones((height, width, 3), dtype=np.uint8)

for x in range(height):
    for y in range(width):
        val = ones_json[f'{y},{x}']
        data[x, y] = val.split(',')
        
img = Image.fromarray(data, 'RGB')
img.save(png_file)
print('Done')
