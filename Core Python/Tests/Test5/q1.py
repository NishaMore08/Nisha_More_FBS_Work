# A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

D = [2000, 500, 200, 100 , 50, 20, 10, 5]
amount=int(input('Enter amount:'))
for i in range(0,len(D)):
    if(amount>2000):
        amount=amount//i
        print("Minimum number of notes:",amount)

    
    