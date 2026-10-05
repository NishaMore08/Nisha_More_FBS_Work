a=int(input("Enter a side:"))
b=int(input("Enter a side:"))
c=int(input("Enter a side:"))
if(a==b and b==c):
    print("Equilateral triangle.")
elif(a==b or b==c or a==c):
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")