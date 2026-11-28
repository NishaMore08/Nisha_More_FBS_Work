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
        return f'Student id:{self.sid} Student Name:{self.sname} Age={self.age} Percentage:{self.percentage}'

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
    
class EnggStudent(Student):
    def __init__(self, sid, sname, age, percentage,branch,internal_marks):
        super().__init__(sid, sname, age, percentage)
        self.branch=branch
        self.internal_marks=internal_marks

    def accept(self):
        super().accept()
        self.branch=input('Enter branch:')
        self.internal_marks=int(input('Enter internal marks:'))

    def display(self):
        return super().display() + f' Branch:{self.branch} Internal Marks:{self.internal_marks}'

    def calRank(self):
        total=((self.percentage*500)/100)+self.internal_marks
        if(total>75):
            print('Distinction') 
        elif(total>60):
            print('First Class') 
        elif(total>50):
            print('Second Class') 
        elif(total>35):
            print('Pass')
        else:
            print('Fail') 

    def __str__(self):
        return f'{self.sname} scored {((self.percentage*500)/100)+self.internal_marks} marks'

e=EnggStudent(101,'Nisha',22,80,'Computer Science',80)
e.accept()
e.display()
e.calRank()
print(e)