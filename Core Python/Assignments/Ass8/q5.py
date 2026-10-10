def sumOfPrime():
    n=int(input('Enter number till you want the sum:'))
    sum=0
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if(i%j==0):
                break
        else:
            sum+=i
    print('Sum of series:',sum)
               
sumOfPrime()