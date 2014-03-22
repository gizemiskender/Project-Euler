

def facti(number):
    result = 1
    while number != 1:
        result *= number
        number -= 1
    return result

print facti(5)

# recursion solve


def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n

number = fact(100)
result = 0
for i in str(number):
    result += int(i)

print result

