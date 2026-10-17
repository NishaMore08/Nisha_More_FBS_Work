li1=[10,20,30,20,40,60,60,20]
li2=[]

for ele in li1:
    if ele not in li2:
        li2+=[ele]

print('After removing duplicate elements:',li2)