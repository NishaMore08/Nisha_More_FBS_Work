str=input('Enter a string:')
letter=0
digit=0
for i in str:
    if(i.isalpha()):
        letter+=1
    elif(i.isdigit()):
        digit+=1

print(f'Total Number of digits are {digit} and Total Number of letters are {letter}.')