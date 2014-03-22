

def func(start):
    l = []
    i = 0
    while(i==0):
        if start % 2 == 0:
            result = start / 2
        else:
            result = start * 3 + 1
        l.append(result)

        if result == 1:
            i = 1

func(13)

