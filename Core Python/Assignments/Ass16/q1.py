class Book:
    count=0
    def __init__(self,bid=101,bname='Hello',price=300,author='Unknown'):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        Book.count+=1

    def ShowBook(self):
        print(f'Book Id:{self.bid} Book Name:{self.bname} Price:{self.price} Author:{self.author}')

    def __del__(self):
        self.bid=None
        self.bname=None
        self.price=None
        self.author=None

    @staticmethod
    def ShowCount():
        print(f'Count of objects:{Book.count}')

b1=Book()
b2=Book(11,'God',700,'Nisha')
b3=Book(23,'Hii',400,'Unknown')

b1.ShowBook()
b2.ShowBook()
b3.ShowBook()

Book.ShowCount()