class Shirt:
    def __init__(self,sid=11,sname='Linen',type='Plane',price=800,size='Small'):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size

    def ShowShirt(self):
        print(f'Shirt Id:{self.sid} Shirt Name:{self.sname} Type:{self.type} Price:{self.price} Size={self.price}')

    def __del__(self):
        self.sid=None
        self.sname=None
        self.type=None
        self.price=None
        self.size=None

s1=Shirt()
s2=Shirt(10,'Linen','Formal',700,'Large')

s1.ShowShirt()
s2.ShowShirt()