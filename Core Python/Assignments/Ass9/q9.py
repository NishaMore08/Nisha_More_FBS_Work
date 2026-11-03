def power(m,n):
    if(n==0):
        return 1
    else:
        return m*power(m,n-1)

m=int(input('Enter the base:'))
n=int(input('Enter the power:'))

print('Result:',power(m,n))