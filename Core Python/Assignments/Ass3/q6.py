C_P=int(input("Enter cost price:"))
S_P=int(input("Enter Selling price:"))
if(C_P > S_P):
    print("Loss.")
elif(S_P > C_P):
    print("Profit.")
else:
    print("No Profit,No Loss.")