n=int(input("Enter a number:"))
sum=0
temp=n
while(n>0):
    d=n%10
    n=n//10
    fact=1
    for i in range(1,d+1):
        fact*=i
    sum+=fact
if(sum==temp):
    print(f"{temp} is a strong number.")
else:
    print(f"{temp} is not a strong number.")