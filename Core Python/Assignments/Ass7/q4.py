for i in range(1,6):
    for k in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(i+j-1,end=' ')
    for j in range(i-1,0,-1):
        print(i+j-1,end=' ')

    print()