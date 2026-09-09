num=int(input("Enter a three-digit number:"))

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10

print("Digits are:",d3,d2,d1)

sum=d1+d2+d3

print("Sum of entered three-digit number is:",sum)