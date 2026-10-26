n=int(input("Enter the number of coins:"))
l=list(map(int,input('Enter the coin numbers:').split()))

for i in l:
    if l.count(i)%2!=0:
        print('Missing coin number:',i)
        break
