m1=int(input("Enter marks of sub 1:"))
m2=int(input("Enter marks of sub 2:"))
m3=int(input("Enter marks of sub 3:"))
m4=int(input("Enter marks of sub 4:"))
m5=int(input("Enter marks of sub 5:"))

total=m1+m2+m3+m4+m5
percentage=(total/500)*100
print("Percentage:",percentage)

if(percentage>=75):
    print("Grade: Distinction")
elif(percentage>=60):
    print("Grade: First Class")
elif(percentage>=50):
    print("Grade: Second Class")
elif(percentage>=35):
    print("Grade: Pass")
else:
    print("Grade: Fail")