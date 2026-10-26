D = [2000, 500, 200, 100 , 50, 20, 10, 5]
amount=int(input('Enter amount:'))
total_notes=0
for note in D:
    count=amount//note
    if(count>0):
        print(note,":",count,"notes")
        total_notes+=count
        amount=amount%note

print('Minimum number of notes:',total_notes)

    
    