def bubbleSort(li):
    size=len(li)
    for i in range(1,3):
        for j in range(0,size-i):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
    return li[size-2]

li=[38,29,48,53,28,20]
res=bubbleSort(li)
print('Second largest element from list:',res)

