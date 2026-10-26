di={1:'Python',2:'Java',3:'C'}
key=int(input('Enter a key to check:'))
if key in di.keys():
    print(f'{key} exists in dictionary.')
else:
    print(f'{key} does not exist in dictionary.')