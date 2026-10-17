li=[98,28,41,63,10]

max=li[0]
min=li[0]

for i in range(1,len(li)):
    if(li[i]>max):
        max=li[i]
    elif(li[i]<min):
        min=li[i]

print('Max:',max)
print('Min:',min)