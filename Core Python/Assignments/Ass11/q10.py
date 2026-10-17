li=[1,2,3,4,5,6,7,8,9,10]

for ele in li:
    if(ele%2==0):
        li.remove(ele)

print('List after removing even numbers:',li)