def palindrome():
    n=int(input('Enter a number:'))
    temp=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if(rev==temp):
        print(f'{temp} is a palindrome number.')
    else:
        print(f'{temp} is not a palindrome number.')

palindrome()