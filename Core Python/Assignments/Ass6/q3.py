n=int(input('Enter number of rows:'))
for i in range(n):
    for j in range(1,4-i):
        print(' ',end=' ')

    num=1
    for j in range(i+1):
        print(num,' ',end=' ')
        num=num*(i-j)//(j+1)
    print()