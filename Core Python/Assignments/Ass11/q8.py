n=1
for i in range(1,11):
    li=[]
    for j in range(1,11):
        li+=[n]
        n+=1
    if(i%2==0):
        li.reverse()

    print(li)