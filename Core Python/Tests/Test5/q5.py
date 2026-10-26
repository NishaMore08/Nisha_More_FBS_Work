# Python Program to Find the Union of two Lists without
# using set concept.

li1=[1,2,3,4,9,5]
li2=[6,7,3,9,2,0]
li3=[]
for i in li1:
    for j in li2:
        if j not in li1:
            li3+=[j]
print('Union of two list:',li3)