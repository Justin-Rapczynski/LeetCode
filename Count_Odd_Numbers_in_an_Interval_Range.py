#Testing code
def countOdds(low, high):
    N = (high - low) // 2
    if (high % 2 != 0 or low % 2  != 0):
        N += 1
    return(N)

output = 0
low = 3
high = 7


countOdds(low, high)


#First Answer (To slow)
#class Solution(object):
#    def countOdds(self, low, high):
 #       output = 0
 #       count = True
 #       while count == True:
  #          if low > high:
  #              count = False
   #         elif low <= high and low % 2 != 0:
    #            output = output + 1
     #           low = low +1
#
     #       elif low % 2 == 0:
     #           low = low + 1

     #   return(output)   
        


#ACCEPTED ANSWER