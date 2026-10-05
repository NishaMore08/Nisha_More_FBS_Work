n=int(input("Enter how many terms you want:"))
x=int(input("Enter a number:"))
sum=0
k=1
for i in range(1,n+1):
    if(i%2==0):
        sum-=(x*i)/k
    else:
        sum+=(x*i)/k
    k+=2
    
print("Sum of series:",sum)