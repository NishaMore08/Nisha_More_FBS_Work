def sum_num(n):
    if(n==0):
        return 0
    else:
        return n+sum_num(n-1)

n=int(input('Enter a number:'))
print('Sum:',sum_num(n))