li=[1,2,3,4,5,6,7,8,9,10]
li1=[]
li2=[]
for ele in li:
    if(ele%2==0):
        li1.append(ele)
    else:
        li2.append(ele)

print('Even number list:',li1)
print('Odd number list:',li2)