li=[28,15,39,20,98,100,48]

min=li[0]
for ind in range(1,len(li)):
    if(li[ind]<min):
        min=li[ind]

print('Min:',min)