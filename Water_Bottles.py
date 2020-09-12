def numWaterBottles(numBottles, numExchange):

    numEmpty = 0
    numDrank = 0
    numEmpty += numBottles
    numDrank += numBottles
    while numEmpty >= numExchange:
        numDrank += numEmpty // numExchange
        numEmpty = (numEmpty - (numExchange * (numEmpty // numExchange))) + (numEmpty // numExchange)

    return(numDrank)

numBottles = 15
numExchange = 4
numWaterBottles(numBottles, numExchange)


#ACTUAL ACCEPTED ANSWER

#class Solution(object):
 #   def numWaterBottles(self, numBottles, numExchange):
  #      numEmpty = 0
   #     numDrank = 0
    #    numEmpty += numBottles
     #   numDrank += numBottles
      #  while numEmpty >= numExchange:
       #     numDrank += numEmpty // numExchange
        #    numEmpty = (numEmpty - (numExchange * (numEmpty // numExchange))) + (numEmpty // numExchange)
       # return(numDrank)