li=[1,3,4,1,2,3,6,7,1,2,4]
dict={}
for number in li:
    dict[number]=li.count(number)

print('Frequency of numbers:',dict)