def fun1():
    temp=n
    d=0
    while(temp>0):
        d=d+1
        temp=temp//10
    return d

def fun2():
    temp=n
    sum=0
    while(temp>0):
        digit=temp%10
        power=1
        for i in range(res1):
            power*=digit

        sum+=power
        temp=temp//10

    return sum

def fun3():
    if(res2==n):
        print(f'{n} is an armstrong number.')
    else:
        print(f'{n} is not an armstrong number.')

n=int(input('Enter a number:'))
res1=fun1()
res2=fun2()
fun3()