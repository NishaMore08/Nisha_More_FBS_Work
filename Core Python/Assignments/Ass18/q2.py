class Distance:
    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm

    def __del__(self):
        self.km=None
        self.m=None
        self.cm=None

    def __add__(self,other):
        km=self.km+other.km
        m=self.m+other.m
        cm=self.cm+other.cm
        return km,m,cm

    def __sub__(self,other):
        km=self.km-other.km
        m=self.m-other.m
        cm=self.cm-other.cm
        return km,m,cm

d1=Distance(20,5,100)
d2=Distance(35,4,250)

print(d1+d2)
print(d1-d2)