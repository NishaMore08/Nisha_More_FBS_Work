A=int(input("Enter 1st angle:"))
B=int(input("Enter 2nd angle:"))
C=int(input("Enter 3rd angle:"))
sum=0
if(A>0 and B>0 and C>0):
    sum=A+B+C
    if(sum==180):
        print("Triangle is valid.")
    else:
        print("Triangle is not valid.")
else:
    print("Triangle is not valid.")