def sepDigit(n):
    if(n>0):
        d=n%10
        print(d,end=' ')
        sepDigit(n//10)

n=153
sepDigit(n)
