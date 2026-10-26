li1=[1,2,3,4,9,5]
li2=[6,7,3,9,2,0]
li3=[]
for i in li1:
    if i not in li3:
            li3.append(i)

for i in li2:
    if i not in li3:
            li3.append(i)
print('Union of two list:',li3)