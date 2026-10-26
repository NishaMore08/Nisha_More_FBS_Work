str=input('Enter a string:')
li=str.split()
dict={}
for word in li:
    dict[word]=li.count(word)

print(dict)