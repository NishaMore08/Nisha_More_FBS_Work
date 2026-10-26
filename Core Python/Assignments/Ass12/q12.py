str=input('Enter a string:')
count=0
for i in range(0,len(str)):
    if(str[i].islower()):
        count+=1

print('Number of lowercase characters:',count)