n=int(input('Enter till how many numbers you want to calculate sum:'))
sum=0
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    sum+=i/fact

print('Sum of series:',sum)
