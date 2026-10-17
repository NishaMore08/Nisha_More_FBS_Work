#1
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()



# for i in range(1,6):
#     for j in range(1,6):
#         if(i%2==0):
#             print("$",end=" ")
#         else:
#             print("*",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if(i==1 or i==5 or j==1 or j==5):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if(i==5 or i==j or j==1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if(i==1 or j==1 or i+j==6):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# for i in range(1,6):
#     for j in range(6-i,0,-1):
#         if(i==1 or j==1 or i+j==6):
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")

#     for j in range(1,i+1):
#         print("*",end=" ")

#     print()

# k=1
# for i in range(1,6):
#     for i in range(1,6):
#         print(k,end=" ")
#         k+=1
#     print()



# for i in range(1,7):
#     for j in range(1,7):
#         if(i==1 or i==6 or j==1 or j==6):
#             print("*",end=" ")
#         else:
#             print(i+j-1,end=" ")
#     print()




for i in range(1,8):

    for j in range(1,5-i):
        print("*",end=" ")

    for j in range(1,i-3):
            print("*",end=" ")

    for j in range(1,8):
        if(i==4 and j%2!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    for j in range(1,8):
            if(j==4 and i%2!=0):
                print("*",end=" ")
            else:
                print(" ",end=" ")

    print()
