import string
roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


# integer to Roman

strnumber = raw_input("please enter a integer number...  ")

result = ""
number = int(strnumber)

for i, v in enumerate(values):
    while (number >= v):
        number -= v
        result += roman[i]
print result

# Roman to integer

s = str(raw_input('please enter a roman number... '))

sum = 0


while s:
    if len(s) == 1:
        sum = romanDict[s[0]]
        break
    if romanDict[s[0]] >= romanDict[s[1]]:
        sum += romanDict[s[0]]
        s = s[1:]
    else:
        sum += romanDict[s[1]] - romanDict[s[0]]
        s = s[2:]
print sum











