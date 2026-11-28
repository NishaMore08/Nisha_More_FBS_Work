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
    
class College(Student):
    def __init__(self, sid, sname, age, percentage,No_of_students):
        super().__init__(sid, sname, age, percentage)
        self.No_of_students=No_of_students

    def accept(self):
        self.No_of_students=int(input('Enter number of students:'))

    def display(self):
        print(f'No of students:{self.No_of_students}')

    def removeStudent(self):
        removestud=int(input('How much students to remove:'))
        self.No_of_students=self.No_of_students-removestud
        print('Student removed successfully')
        print('Total students:',self.No_of_students)
        
    def __str__(self):
        return f'No of students:{self.No_of_students}'

c=College(11,'Nisha',22,80,20)
c.accept()
c.display()
c.removeStudent()
print(c)    

                                                              