x = 1
temp = 1
result = 0
sum = 0
while sum < 4000000:
    sum = temp + x
    temp = x
    x = sum
    if sum % 2 == 0:
        result = sum + result
        print result
