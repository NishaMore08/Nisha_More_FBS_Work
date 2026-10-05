for i in range(1,50):
    temp=i
    d=0
    while(temp>0):
        d=d+1
        temp=temp//10
    temp=i
    sum=0
    while(temp>0):
        digit=temp%10
        power=1
        for j in range(d):
            power=power*digit
        sum=sum+power
        temp=temp//10
    if(sum==i):
        print(i,end=' ')