import math

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
    
    while largestSquare >= 2:
        i = 1
        while largestSquare * i < n:
            j = 0
            currentLargestSquare = largestSquare
            while j < 4 -i: 
                while(sum(retList) + currentLargestSquare <= n and len(retList) <= 3):
                    retList.append(currentLargestSquare)
                    j += 1
                if n - sum(retList) != 0 and len(retList) == 4:
                    break
                elif n - sum(retList) <= (3 - j):
                    return(addZerosAndOnes(retList, n))
                currentLargestSquare = ((currentLargestSquare ** .5) - 1) ** 2
            i += 1
            largestSquare = (largest - 1) ** 2
        retList = []
    
    return ("Not found")        # Should never excecute, but just in case LaGrange was wrong...

while(True):
    print(str(lagrange4squares(int(input()))))