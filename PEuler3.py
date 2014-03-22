from math import sqrt

def IsPrime ( num ):
    m = 0
    if num == 2:
        return True
    else:
        for i in range(2, int(sqrt(num))):
            if num % i == 0:
                m = 1
            if m > 0:
                return False
            else:
                return True

def Factor(x):
    for i in range(2, int(sqrt(x))):
        if x % i == 0 and IsPrime(i):
            print i

Factor (600851475143)
#print IsPrime(4)
