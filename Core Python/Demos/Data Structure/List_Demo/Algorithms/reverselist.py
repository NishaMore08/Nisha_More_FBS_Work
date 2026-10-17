# li=[10,20,30,40,50,60,70,80,90,100]
# #swap to reverse the list 
# #like swap 10 with 100 ,20 with 90

# def reverseList(li):
#     size=len(li)
#     for i in range(0,size-1):
#         min_ind=i
#         for j in range(i+1,size):
#             if(li[j]<li[j+1]):
#                 min_ind=j
#         li[i],li[min_ind]=li[min_ind],li[i]
        
# li=[10,20,30,40,50,60,70,80,90,100]
# reverseList(li)
# print('Reversed list:',li)
