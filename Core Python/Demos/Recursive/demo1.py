def fun(n):
    # print('Function executing.')
    print(n,end=' ')
    if(n>1):
        fun(n-1)

n=5
fun(n)


# def fun(n):
#     if(n>0):
#         print('Function executing')
#         fun(n-1)

# n=5
# fun(n)