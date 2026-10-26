d1={}
n=int(input('Enter how many numbers you want:'))
for i in range(1,n+1):
    d1.update({i:i*i})

print(d1)