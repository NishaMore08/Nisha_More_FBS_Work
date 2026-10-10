def exponential():
    n=int(input('Enter number till you want the sum:'))
    sum=0
    for i in range(1,n+1):
        exp=i**i
        sum+=exp
    print('Sum of series:',sum)

exponential()