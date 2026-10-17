li=[10,20,30,40,50,60,70,80,90,100]
res=li[1:6]    #parameters:start,stop,step
res=li[3:9]    #exclude last index like range
res=li[1:8:2]
res=li[1:8:3]
res=li[8:1:-1]   
res=li[0:6]
res=li[:6]     #by default starts from 0th index
res=li[4:20]
res=li[4:]     #by default goes till last element
res=li[::]    #start to end element,step by +1
res=li[:]     #start to end element,step by +1
res=li[::-1]  #in reverse order
print(res)