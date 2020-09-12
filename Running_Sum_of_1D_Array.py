
    

List = []
def runningSum(nums):

    extraInt = 0 
    for x in nums:
        extraInt += x
        print(extraInt)
        List.append(extraInt)
nums = [1, 2, 3, 4]
runningSum(nums)
print(List)


#Actual Answer

#class Solution(object):
#    def runningSum(self, nums):
#        extraInt = 0 
#        List = []
#        for x in nums:
#            extraInt += x
#            print(extraInt)
#            List.append(extraInt)
#        return(List)