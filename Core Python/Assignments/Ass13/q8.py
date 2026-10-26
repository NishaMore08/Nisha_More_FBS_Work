str=input('Enter a string:')
dict={}
li=str.split()
for word in li:
    dict[word]=li.count(word)

print('Frequency of Words:',dict)
