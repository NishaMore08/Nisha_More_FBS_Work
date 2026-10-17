##check number
# num=int(input("Enter a number:"))
# temp=num
# sum=0
# while(num > 0):
#     d = num % 10
#     # print(d)
#     num = num //10
#     fact=1
#     for i in range(1,d+1):
#         fact*=i
#     # print(fact)
#     sum+=fact
# if(sum==temp):
#     print(f"{temp} is a strong number.")
# else:
#     print(f"{temp} is not a strong number.")


##first n
# n=int(input('How many numbers you want:'))
# count=0
# num=1
# while(count<n):
#     sum=0
#     temp=num
#     while(temp>0):
#         d=temp%10
#         temp=temp//10
#         fact=1
#         for i in range(1,d+1):
#             fact*=i
#         sum+=fact
#     if(sum==num):
#         print(num,end=' ')
#         count+=1
#     num+=1



##between range
for i in range(1,201):
    temp=i
    sum=0
    while(i>0):
        d=i%10
        i=i//10
        fact=1
        for j in range(1,d+1):
            fact*=j
        sum+=fact
    if(sum==temp):
        print(temp,end=' ')
