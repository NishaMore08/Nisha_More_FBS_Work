li=[10,20,30,20,40,20]
num = int(input("Enter the number to search: "))

count = 0

for i in li:
    if i == num:
        count += 1

if count > 0:
    print("Element is present in the list.")
    print("It occurs", count, "times.")
else:
    print("Element is not present in the list.")