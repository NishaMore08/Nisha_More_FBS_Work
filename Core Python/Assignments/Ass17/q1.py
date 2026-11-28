class Student:
    def __init__(self,sid,sname,age,percentage):
        self.sid=sid
        self.sname=sname
        self.age=age
        self.percentage=percentage

    def accept(self):
        self.sid=int(input('Enter id:'))
        self.sname=input('Enter name:')
        self.age=int(input('Enter age:'))
        self.percentage=int(input('Enter percentage:'))

    def display(self):
        print(f'Student id:{self.sid} Student Name:{self.sname} Age={self.age} Percentage:{self.percentage}')
    def calRank(self):
        if(self.percentage>90):
            print('Rank:1')
        elif(self.percentage>80):
            print('Rank:2')
        elif(self.percentage>70):
            print('Rank:3')
        elif(self.percentage>60):
            print('Rank:4')
        elif(self.percentage>50):
            print('Rank:5')
        elif(self.percentage>35):
            print('Rank:6')
        else:
            print('Fail')
   
    def __str__(self):
        return f'{self.sname} scored {self.percentage}%'

s=Student(1,'Nisha',22,87)

s.accept()
s.display()
s.calRank()
print(s)
        