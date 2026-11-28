class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __del__(self):
        self.real=None
        self.imag=None

    def __add__(self,other):
        r=self.real+other.real
        im=self.imag+other.imag
        return f'{r}+{im}'

    def __sub__(self,other):
        r=self.real-other.real
        im=self.imag-other.imag
        return f'{r}-{im}'

c1=ComplexNumber(9,5)
c2=ComplexNumber(7,4)
print(f'{c1+c2}i')
print(f'{c1-c2}i')