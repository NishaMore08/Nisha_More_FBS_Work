N=int(input("Enter a number:"))
sum=0
for i in range(1,N+1):
    Expo=N**i
    sum+=Expo
print("Sum of series:",sum)