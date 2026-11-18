class Book:
    def __init__(self,bid=110,bname='God',price=400,author='Unknown'):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author

    def Showbook(self):
        print(f'Book Id:{self.bid} Book Name:{self.bname} Price:{self.price} Author:{self.author}')

    def __del__(self):
        self.bid=None
        self.bname=None
        self.price=None
        self.author=None

b1=Book()
b2=Book(101,'Stranger Things',300,'Nisha')

b1.Showbook()
b2.Showbook()


        