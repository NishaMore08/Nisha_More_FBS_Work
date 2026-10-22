n=int(input('Enter number of employees:'))
total_emp_salary=0
for i in range(1,n+1):
    basic=int(input('Enter basic salary:'))
    if(basic<20000):
        da=(10/100)*basic
        ta=(12/100)*basic
        hra=(15/100)*basic
    else:
        da=(15/100)*basic
        ta=(18/100)*basic
        hra=(20/100)*basic

    total_salary=basic+da+ta+hra
    print(f'Total salary of emp {i}:',total_salary)

    total_emp_salary+=total_salary

print('Total salary of all employees:',total_emp_salary)



