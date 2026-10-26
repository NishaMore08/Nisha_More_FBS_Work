str=input('Enter a string:')
n=int(input('Enter an index to remove the element:'))
for i in range(0,len(str)):
    if(i==n):
        continue
    print(str[i],end='')