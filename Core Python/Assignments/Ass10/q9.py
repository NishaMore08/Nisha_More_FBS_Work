li=[1,2,3,4,5,6,7]

even_list=list(filter(lambda n:n%2==0,li))
odd_list=list(filter(lambda n:n%2!=0,li))

print('Even number list:',even_list)
print('Odd number list:',odd_list)