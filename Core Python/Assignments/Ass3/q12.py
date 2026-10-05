num=int(input("Enter 3 digit number:"))
temp=num
reverse=0
while(num>0):
    d=num%10
    reverse=reverse*10+d
    num=num//10

if(reverse==temp):
    print("Palindrome number.")
else:
    print("Not a Palindrome number.")
