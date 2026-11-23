D = [2000, 500, 200, 100 , 50, 20, 10, 5]

amount=int(input('Enter amount:'))
total_notes=0
for i in D:
    if(amount>0):
        notes=amount//i
        total_notes+=notes
        print(f'{i}:{notes}')
        amount=amount%i

print('Minimum number of notes:',total_notes)


    
    