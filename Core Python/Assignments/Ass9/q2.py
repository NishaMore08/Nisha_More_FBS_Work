def count_digits(n):
    if(n==0):
        return 0
    return 1+count_digits(n//10)

def armstrong(n,digits):
    if(n==0):
        return 0
    digit=n%10
    return digit**digits+armstrong(n//10,digits)

num=int(input('Enter a number:'))
digits=count_digits(num)
if armstrong(num,digits)==num:
    print('Armstrong number')
else:
    print('Not an Armstrong number')