# tu=(10,20,20,30,3.14,'abc')

# # # tu=(10,)           #type=tuple
# # tu=10,20,30,40
# # tu=(10)              #type=int

# # tu[0]=50   #raise error

# print(type(tu))
# print(tu)


#tuple is faster than list
import sys

tu=()
li=[]
print(sys.getsizeof(tu))
print(sys.getsizeof(li))