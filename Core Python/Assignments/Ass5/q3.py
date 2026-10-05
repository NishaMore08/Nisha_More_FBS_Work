n=int(input("Enter number of passengers:"))
ticket=int(input("Enter per ticket cost:"))
total=0
for i in range(1,n+1):
    age=int(input(f"Enter age of person{i}:"))
    if(age<12):
        amount=ticket*(30/100)
    elif(age>59):
        amount=ticket*(50/100)
    else:
        amount=ticket
    total+=amount
print("Total amount to ticket to travel:",total)
