import json

with open('lock.json', 'r') as js:
    zero_json = js.read()
zero_json = json.loads(zero_json)

vjs = zero_json.values()
kjs = zero_json.keys()

sort_vjs = list(vjs)
sort_kjs = list(kjs)

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

out = ob.solve(sort_vjs)
final = ob.solve(out)
# print(out)
print(out == final)
