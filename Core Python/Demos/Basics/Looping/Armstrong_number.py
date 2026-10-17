##check number
# n=int(input('Enter a number:'))
# temp=n
# digits=0
# sum=0
# while(temp>0):
#     digits=digits+1
#     temp=temp//10

# temp=n
# while(temp>0):
#     digit=temp%10
#     power=1
#     for i in range(digits):
#         power*=digit
#     sum+=power
#     temp=temp//10

# if(sum==n):
#     print('Armstrong number.')
# else:
#     print('Not Armstrong number.')


##first n
n=int(input('How many numbers you want:'))
count=0
num=1

while(count<n):
    temp=num
    d=0
    while(temp>0):
        d=d+1
        temp=temp//10

    temp=num
    sum=0
    while(temp>0):
        digit=temp%10
        power=1
        for i in range(d):
            power*=digit
        sum+=power
        temp=temp//10

if(sum==num):
    print(sum,end=' ')
    count+=1
num+=1


