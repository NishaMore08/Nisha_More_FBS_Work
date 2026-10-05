n=int(input("Enter number of students:"))
sum=0
for i in range(1,n+1):
    total=0
    print(f"Enter marks of student {i}")
    for j in range(1,6):
        m=int(input(f"Enter marks of sub {j}:"))
        total+=m
    
    percentage=(total/500)*100
    print(f"Percentage of student {i}:",percentage)

    sum+=percentage

Average_percentage=sum/5
print("Average percentage of students:",Average_percentage)