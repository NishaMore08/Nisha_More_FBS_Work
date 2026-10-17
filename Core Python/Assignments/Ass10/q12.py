number_list=[]
for i in range(1,6):
    number_list+=[i]

print('List with numbers:',number_list)

square_list=list(map(lambda n:n**2,number_list))
cube_list=list(map(lambda n:n**3,number_list))

print('List with square of numbers:',square_list)
print('List with cube of numbers:',cube_list)