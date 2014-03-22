

def fibo(n):
    result = 0
    s = 1
    i = 0
    if n < 2:
        return 1
    for i in range(n):
        result = i + s
        i = s
        s = result
    return result

#i=0
#while len(str(fibo(i))) < 1000:
    #fibo(i)
    #print i
    #i += 1

n = 1
while True:
    f = fibo(n)
    if len(str(f)) >= 1000:
        print("#%d: %d" % (n, f))
        exit()
    n += 1

#def fib(n):
    #if n <= 3:
        #return 1
    #else:
        #return fib(n-2) + fib(n-1)








