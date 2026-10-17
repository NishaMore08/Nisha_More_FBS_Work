li=[10,29,48,38,19]

max=li[0]
smax=0

for ind in range(1,len(li)):
    if(li[ind]>max):
        smax=max
        max=li[ind]
    elif(li[ind]>smax):
        smax=li[ind]

print('Second largest element:',smax)