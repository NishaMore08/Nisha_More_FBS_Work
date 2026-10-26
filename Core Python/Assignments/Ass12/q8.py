str=input('Enter a string:')
for i in range(0,len(str)):
    if(i%2!=0):
        continue
    print(str[i],end=' ')
