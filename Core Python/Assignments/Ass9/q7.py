def SumofDigit(n):
    if(n==0):
        return 0
    else:
        d=n%10
        return d+SumofDigit(n//10)

n=int(input('Enter a number:'))
print('Sum of Digit:',SumofDigit(n))