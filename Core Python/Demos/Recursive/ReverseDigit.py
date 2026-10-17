def revDigit(n,r=0):
    if(n==0):
        return r
    d=n%10
    r=r*10+d
    return revDigit(n//10,r)

n=123
res=revDigit(n)
print(res)