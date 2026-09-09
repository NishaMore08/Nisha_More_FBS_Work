##operators
x=10
y=20
a='abc'
b='def'

#+
res=x+y
res=a+b

#-
res=y-x

#*
res=x*y

#/
res=5/2

#//(gives output till digit)
res=5//2

#%
res=5%2

#**
res=4**3
# print(res)

# num1=int(input("Enter number 1:"))
# num2=int(input("Enter number 2:"))

# sum=num1+num2

# print(f'Addition of {num1} and {num2} is {sum}.')

##separate digits
num=int(input("Enter a number:"))
d1=num%10
num=num//10
d2=num%10
num=num//10
d3=num%10
num=num//10
print("Digits of given number are:",d3,d2,d1)
print("num:",num)

