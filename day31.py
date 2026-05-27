# Recurssion using parameter...

# print x,n times,using the tail

# def func(x,n):
#     if n==0:
#         return
#     print(x)
#     func(x,n-1)

# func(15,4)



# print 1 go n using recursions 
# tail recursions.

# def func(i,n):
#     if i>n:
#         return 
#     print(i)
#     func(i+1,n)

# func(1,5)


# print 1 go n using recursions 
# head recursions

# def func3(n):
#     if n==0:
#         return
#     func3(n-1)
#     print(n)

# func3(1,5)




# print n go 1 using recursions 
# using head
# def func2(x,n):
#     if x>n:
#         return
#     func2(x+1,n)
#     print(x)
# func2(1,7)

# print n go 1 using recursions 
# using tail..

# def func4(x,n):
#     if n<x:
#         return
#     print(n)
#     func4(x,n-1)

# func4(1,7)


# sum of 1 to N

# def func(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i,i+1,n)

# func(0,1,4)

# sum of 1 to n uing functional recursions...
# def func(n):
#     if n==1:
#         return 1
#     return n+func(n-1)

# print(func(5))

#  find the factoreal of a number.

# def func(n):
#     if n==1:
#         return 1
#     return n*func(n-1)
# print(func(5))