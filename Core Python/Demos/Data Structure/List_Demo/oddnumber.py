li=[3,9,70,14,1,2,6,17]

count=0
for ind in range(0,len(li)):
        if(li[ind]%2!=0):
            count+=1
            if(count%2!=0):
                print(li[ind])
                