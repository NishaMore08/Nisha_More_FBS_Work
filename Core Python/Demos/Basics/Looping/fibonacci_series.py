##check number
n=int(input('Enter a number:'))
a=-1
b=1
while(a<=n):
    if(a==n or b==n):
        print(f'{n} is a fibonacci number.')
        break
    c=a+b
    a=b
    b=c

else:
    print(f'{n} is not a fibonacci number.')


# ##first n
# n=int(input('How many numbers you want:'))
# a=-1
# b=1
# for i in range(n):
#     c=a+b
#     print(c,end=' ')
#     a=b
#     b=c


##between range
# a=0
# b=1
# for i in range(1,10):
#     c=a+b
#     if(c==i):
#         print(i,end=' ')
#         a=b
#         b=c

