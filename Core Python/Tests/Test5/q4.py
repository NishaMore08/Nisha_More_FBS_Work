li=[1,3,4,1,2,3,6,7,1,2,4]
dict={}
for i in li:
    dict[i]=li.count(i)

print('Frequency of numbers:',dict)