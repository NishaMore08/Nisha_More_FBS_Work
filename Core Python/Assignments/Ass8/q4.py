def sumOfOdd():
    n=int(input('Enter number till you want the sum:'))
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum+=i
    print('Sum of all odd numbers:',sum)

sumOfOdd()
