amt=int(input("Enter amount:"))

n2000=amt//2000
amt=amt%2000

n500=amt//500
amt=amt%500

n200=amt//200
amt=amt%200

n100=amt//100
amt=amt%100

n50=amt//50
amt=amt%50

n20=amt//20
amt=amt%20

n10=amt//10
amt=amt%10

n5=amt//5
amt=amt%5

n2=amt//2
amt=amt%2

n1=amt//1

total=n2000+n500+n200+n100+n50+n20+n10+n5+n2+n1
print("Minimum number of notes=",total)