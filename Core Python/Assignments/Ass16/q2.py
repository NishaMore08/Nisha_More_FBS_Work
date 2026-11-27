class Product:
    discount=10
    def __init__(self,pid=11,pname='Brush',price=100,quantity=400):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def ShowProduct(self):
        print(f'Product Id:{self.pid} Product Name:{self.pname} Price:{self.price} Quantity:{self.quantity}')

    def __del__(self):
        self.pid=None
        self.pname=None
        self.price=None
        self.quantity=None

    @staticmethod
    def Applydis(self):
        discount_amt=self.price*(Product.discount/100)
        self.price=self.price-discount_amt
        print(f'Total Price:{self.price}')

p1=Product()
p2=Product(101,'Soap',50,200)
p3=Product(110,'Perfume',300,100)

p1.ShowProduct()
p2.ShowProduct()
p3.ShowProduct()

Product.Applydis(p3)