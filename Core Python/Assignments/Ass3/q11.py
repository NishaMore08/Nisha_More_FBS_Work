total=0
ticket=int(input("Enter ticket amount:"))
for i in range(1,6):

    age=int(input("Enter age of person:"))

    if(age < 12):
        amount=ticket*(30/100)
    elif(age>59):
        amount=ticket*(50/100)
    else:
        amount=ticket

    total+=amount
print("Total amount:",total)