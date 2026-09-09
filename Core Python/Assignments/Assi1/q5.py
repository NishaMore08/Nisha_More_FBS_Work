#5
P=int(input("Enter principal amount:"))
t=int(input("Enter time:"))
r=float(input("Enter rate of interest:"))
n=int(input("Enter number of compounding periods:"))
A=P*(1+r/n)**(n*t)
print("Compound Interest:",A)