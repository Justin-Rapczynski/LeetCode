
def twoSum(nums, target):
    if len(nums) < 2:
        pass
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sums = nums[i] + nums[j]
            if sums == target:
                return[i, j]



nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))


#ACTUAL ACCEPTED FULL ANSWER
#class Solution(object):
  #  def twoSum(self, nums, target):
  #      if len(nums) < 2:
  #          pass
  #      for i in range(len(nums)):
   #         for j in range(i+1, len(nums)):
  #              sums = nums[i] + nums[j]
     #           if sums == target:
     #               return[i, j]   