def sumOfDigit(n):
    if(n<=0):
        return 0
    else:
        d=n%10
        return d+sumOfDigit(n//10)

n=123
res=sumOfDigit(n)
print(res)