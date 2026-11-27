class Shirt:
    price=1000
    def __init__(self,sid=101,sname='Linen',type='Formal',size='Small'):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.size=size

    def showShirt(self):
        print(f'Shirt Id:{self.sid} Shirt Name:{self.sname} Shirt Type:{self.type} Shirt Size:{self.size}')

    def __del__(self):
        self.sid=None
        self.sname=None
        self.type=None
        self.size=None

    @staticmethod
    def CalPrice(self):
        if(self.size!='Small'):
            Shirt.price=Shirt.price+(Shirt.price*(10/100))
            print(f'Shirt Price:{Shirt.price}')
        else:
            print(f'Shirt Price:{Shirt.price}')

s1=Shirt()
s2=Shirt(110,'Checks','Plain','Medium')
s1.showShirt()
s2.showShirt()

Shirt.CalPrice(s2)
        
        