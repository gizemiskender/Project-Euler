import urllib
x = urllib.urlopen("https://projecteuler.net/project/names.txt").read()


d = {'"': 0,' ': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
        'I': 9,
        'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19,
        'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
s = {}
k = {}
s = x.split(',')
l = []
for i in s:
    l.append(i)

l.sort()
s = 0
mux = 1
count = 0
result = 0

for i in l:
    toplam = 1
    for k in i:
        s = s + d[k]
    count = count + 1
    mux = s * count
    result = result + mux

    s = 0

print result

