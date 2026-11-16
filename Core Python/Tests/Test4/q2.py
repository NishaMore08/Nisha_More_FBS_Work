def factorial(n,fact):
    if(n<=1):
        return fact
    else:
        fact=fact*n
        return factorial(n-1,fact)

n=int(input('Enter a number:'))
fact=1
res=factorial(n,fact)
print('Factorial:',res)