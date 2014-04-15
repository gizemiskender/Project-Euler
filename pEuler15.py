def fac(number):
    s = 1
    for i in range(1, number + 1):
        s *= i
    return s

print fac(5)

print fac(40)/ (fac(20) * fac(20) )