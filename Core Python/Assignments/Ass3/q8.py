userid=input("Enter user id:")
password=input("Enter password:")

if(userid=="nisha" and password=="8804"):

    print("Correct user id and password.")
    captcha=2814
    print("The verification number is:",captcha)

    number=int(input("Enter the verification number:"))

    if(number==captcha):
        print("Success!!")
    else:
        print("Failed!!")

else:
    print("Invalid user id or password.")
