li=[10,20,30,20,40,60,20]
new_list=[]
given_ele=int(input('Enter an element:'))
for ele in li:
    if(ele==given_ele):
        continue
    else:
        new_list+=[ele]

print('After removing all occurrences of the element')
print('List:',new_list)

