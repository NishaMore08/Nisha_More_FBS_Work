def linearSearch(li,search_ele):
    for ind in range(0,len(li)):
        if(search_ele==li[ind]):
            return ind
    else:
        return -1

li=[29,59,19,59,30,69]
ele=int(input('Enter an element to search:'))
res=linearSearch(li,ele)
if(res!=-1):
    print(f'{ele} is present at index {res}.')
else:
    print(f'{ele} is not present in the list.')