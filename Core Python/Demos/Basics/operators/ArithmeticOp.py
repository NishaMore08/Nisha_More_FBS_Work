# ##operators
# x=10
# y=20
# a='abc'
# b='def'

# #+
# res=x+y
# res=a+b

# #-
# res=y-x

# #*
# res=x*y

# #/
# res=5/2

# #//(gives output till digit)
# res=5//2

# #%
# res=5%2

# #**
# res=4**3
# # print(res)

# # num1=int(input("Enter number 1:"))
# # num2=int(input("Enter number 2:"))

# # sum=num1+num2

# # print(f'Addition of {num1} and {num2} is {sum}.')

# ##separate digits
# num=int(input("Enter a number:"))

# d1=num%10
# num=num//10

# d2=num%10
# num=num//10

# d3=num%10
# num=num//10

# print("Digits of given number are:",d3,d2,d1)
# print("num:",num)







#Arithmetic Operators
#1. +
x=10
y=20

a='abc'
b='def'

#addition of 2 int
res=x+y

#concatenation of 2 str
res=a+b

#subtraction
res=x-y

#multiplication
res=x*y

#division
res=x/y

#floor division
res=x//y

#modulus
res=x%y

#exponential
res=x**y
# print(res)


#Addition of two numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

sum=num1+num2

print(f"The addition of {num1} and {num2} is {sum}.")



#separate out the digits from three digit number
num=int(input("Enter three-digit number:"))

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10

print("Digits are:",d3,d2,d1)




