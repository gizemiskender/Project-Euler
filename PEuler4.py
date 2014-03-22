#polindrome numbers
def IsPolindrome(i):
         letter = str(i)
         if letter == letter[::-1]:
             return True

for i in range(900, 1000):
    for k in range(900, 1000):
        mux = i*k
        if IsPolindrome(mux):
            print mux



