##check number
# n=int(input('Enter a number:'))
# sum=0
# for i in range(1,n//2+1):
#     if(n%i==0):
#         sum+=i
# if(sum==n):
#     print(f'{n} is a perfect number.')
# else:
#     print(f'{n} is not a perfect number.')


##first n
# n=int(input('How many numbers you want:'))
# count=0
# num=1
# while(count<n):
#     sum=0
#     for i in range(1,num//2+1):
#         if(num%i==0):
#             sum+=i
#     if(sum==num):
#         print(num,end=' ')
#         count+=1
#     num+=1


##between range
for i in range(1,51):
    sum=0
    for j in range(1,i//2+1):
        if(i%j==0):
            sum+=j
    if(sum==i):
        print(i,end=' ')