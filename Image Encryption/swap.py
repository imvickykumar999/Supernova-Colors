import numpy as np
from PIL import Image
# import random, json

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

# class Solution:
#    def solve(self, nums):
#       length = len(nums)
#       for i in range(0,length,4):
#          if(i+2<length):
#             nums[i], nums[i+2] = nums[i+2], nums[i]
#          if(i+3<length):
#             nums[i+1], nums[i+3] = nums[i+3], nums[i+1]
#       return nums

# ob = Solution()
# sort_vjs = ob.solve(sort_vjs)

sort_vjs = sorted(sort_vjs, key=len)

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
