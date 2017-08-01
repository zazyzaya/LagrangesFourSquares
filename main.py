import math
import time
import random

def testEfficiency(power):
    
    testNum = math.floor(random.random() * (10 ** power)) + 3 # Must be > 2
    start = time.clock()
    lagrange4squares(testNum)
    end = time.clock()

    return end - start

def addZerosAndOnes(xs, n, listLen=4):
    while(len(xs) < listLen):
        if sum(xs) < n:
            xs.append(1)
        else:
            xs.append(0)

    return xs

def lagrange4squares(n):
    # Lagrange's four-square theorem, also known as Bachet's conjecture, states that every natural number can be 
    # represented as the sum of four integer squares. ie: p = a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2
    # https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem

    largest = math.floor(n ** (1/2))
    largestSquare = largest ** 2
    remainder = n - largestSquare
    retList = []
    minimum = math.floor((n/4) ** .5)   # Smallest that the largest squared number could possibly be
                                        # ie for 100, smallest would be 25 

    while largestSquare >= minimum:
        j = 0
        while j < 4: 
            while(sum(retList) + largestSquare <= n):   
                retList.append(largestSquare)
                j += 1
            if n - sum(retList) != 0 and len(retList) == 4:
                break
            elif n - sum(retList) <= (4 - j):
                return(addZerosAndOnes(retList, n))
            largestSquare = ((largestSquare ** .5) - 1) ** 2
        largestSquare = (largest - 1) ** 2  # Resets initial highest number in set
        largest -= 1    # Keeps track of current highest number
        retList = []
    
    return ("Not found")    # Should never excecute, but just in case LaGrange is wrong...

# powerTimes = []
# for pow in range(14):
#     trialTimes = []
#     for trialNum in range(5):
#         trialTimes.append(testEfficiency(pow + 1))
#
#     print("Finished trial " + str(pow))
#     powerTimes.append(trialTimes)
# 
# print(powerTimes)

while(True):
    print(str(lagrange4squares(int(input()))))