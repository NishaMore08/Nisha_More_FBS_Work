##check number
# num=int(input('Enter a number:'))
# temp=num
# reverse=0
# while(num>0):
#     d=num%10
#     reverse=reverse*10+d
#     num=num//10

# if(reverse==temp):
#     print('Palindrome number.')
# else:
#     print('Not a palindrome number.')


##first n


##Between range
for i in range(10,101):
    temp=i
    rev=0
    while(i>0):
        d=i%10
        rev=rev*10+d
        i=i//10
    if(rev==temp):
        print(temp,end=' ')
