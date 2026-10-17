#1.{}
di={1:'Python',2:'Java',3:'Java','year':2026,1:'PHP'}

#2.Heterogeneous(keys and values both)
#3.Ordered

#4.key:immutable,values:mutable,size-mutable
di['year']=2027
di['age']=30


#5.key:unique,Value:duplication allowed(keys override)
print(type(di))
print(di)