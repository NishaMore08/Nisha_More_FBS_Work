str1=input('Enter string 1:')
str2=input('Enter string 2:')
count1=0
count2=0
for i in str1:
    count1+=1
for j in str2:
    count2+=1

if(count1>count2):
    print('str1 is larger')
else:
    print('str2 is larger')