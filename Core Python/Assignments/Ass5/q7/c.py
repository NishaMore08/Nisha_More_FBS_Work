n=int(input("How many numbers you want:"))
sum=0
for i in range(n):
    num=2**i
    sum+=num
print("Sum of series:",sum)