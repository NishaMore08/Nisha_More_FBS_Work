class Product:
    def __init__(self,pid=32,pname='Perfume',price=400,quantity=700):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def showProduct(self):
        print(f'Product Id:{self.pid} Product Name:{self.pname} Price:{self.price} Quantity:{self.quantity}')

    def __del__(self):
        self.pid=None
        self.pname=None
        self.price=None
        self.quantity=None

p1=Product()
p2=Product(11,'Soap',30,800)

p1.showProduct()
p2.showProduct()