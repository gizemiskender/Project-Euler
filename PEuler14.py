

def collatz(start):
    count = 0
    result = 0
    while result != 1:
        if start % 2 == 0:
            result = start / 2
        else:
            result = start * 3 + 1
        start = result
        count += 1
    return count

def count():
    maxS = 0
    maxi = 0
    i = 1
    while i < 1000000:
        if collatz(i) > maxi:
            maxi = collatz(i)
            maxS = i
        i += 1
    print i
    print collatz(i)
    print maxi
    print maxS

count()