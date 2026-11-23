from abc import ABC,abstractmethod
class Vehicle(ABC):
    extra_charges=0
    def __init__(self,Number_Plate,basic_toll,No_of_Person):
        self.Number_Plate=Number_Plate
        self.basic_toll=basic_toll
        self.No_of_Person=No_of_Person

    @abstractmethod
    def TollCalculation(self):
        pass

class TwoWheeler(Vehicle):
    def __init__(self, Number_Plate, basic_toll, No_of_Person):
        super().__init__(Number_Plate, basic_toll, No_of_Person)

    def __str__(self):
        return f'Number Plate:{self.Number_Plate} Basic Toll:{self.basic_toll} No of Person:{self.No_of_Person}'

    def TollCalculation(self):
        if(self.No_of_Person>2):
            Vehicle.extra_charges=10*self.No_of_Person
        print(f'Toll Calculation:{self.basic_toll+Vehicle.extra_charges}')
    
        
class ThreeWheeler(Vehicle):
    def __init__(self, Number_Plate, basic_toll, No_of_Person):
        super().__init__(Number_Plate, basic_toll, No_of_Person)

    def __str__(self):
        return f'Number Plate:{self.Number_Plate} Basic Toll:{self.basic_toll} No of Person:{self.No_of_Person}'

    def TollCalculation(self):
        if(self.No_of_Person>3):
            Vehicle.extra_charges=20*self.No_of_Person
        print(f'Toll Calculation:{self.basic_toll+Vehicle.extra_charges}')


class FourWheeler(Vehicle):
    def __init__(self, Number_Plate, basic_toll, No_of_Person):
        super().__init__(Number_Plate, basic_toll, No_of_Person)

    def __str__(self):
        return f'Number Plate:{self.Number_Plate} Basic Toll:{self.basic_toll} No of Person:{self.No_of_Person}'

    def TollCalculation(self):
        if(self.No_of_Person>4):
            Vehicle.extra_charges=40*self.No_of_Person
        print(f'Toll Calculation:{self.basic_toll+Vehicle.extra_charges}')


class HeavyVehicle(Vehicle):
    def __init__(self, Number_Plate, basic_toll, No_of_Person):
        super().__init__(Number_Plate, basic_toll, No_of_Person)

    def __str__(self):
        return f'Number Plate:{self.Number_Plate} Basic Toll:{self.basic_toll} No of Person:{self.No_of_Person}'

    def TollCalculation(self):
        if(self.No_of_Person>6):
            Vehicle.extra_charges=100*self.No_of_Person
        print(f'Toll Calculation:{self.basic_toll+Vehicle.extra_charges}')

two=TwoWheeler(1003,20,2)
three=ThreeWheeler(2048,30,3)
four=FourWheeler(3920,40,4)
heavy=HeavyVehicle(2846,60,6)

print(two)
print(three)
print(four)
print(heavy)

two.TollCalculation()
three.TollCalculation()
four.TollCalculation()
heavy.TollCalculation()
