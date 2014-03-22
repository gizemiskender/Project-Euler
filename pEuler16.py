s = str(2 ** 1000)

l = []
for i in s:
    l.append(i)
result = 0
for i in l:
    result += int(i)

print result