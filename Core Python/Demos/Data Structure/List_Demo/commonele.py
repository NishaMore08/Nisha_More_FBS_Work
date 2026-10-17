li1=[1,2,3,4,5,6]
li2=[2,5,3,7,9,10]

for i in range(0,len(li1)):
    for j in range(0,len(li2)):
        if(li1[i]==li2[j]):
            print(li1[i],end=' ')