##Check number
# num=int(input("Enter a number:"))
# if(num>1):
#     for i in range(2,num//2+1):
#         if(num%i==0):
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


##first n
# n=int(input("How many numbers you want:"))

# count=0
# num=2
# while(count<n):
#     for i in range(2,num//2+1):
#         flag=0
#         if(num%i==0):
#             flag=1
#             break

#     else:
#         print(num,end=' ')
#         count+=1

#     num+=1


##Between range
for i in range(2,51):
    for j in range(2,i//2+1):
        if(i%j==0):
            break
    else:
        print(i,end=' ')