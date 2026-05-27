# Number frequency Frequency Counting using Hashing
# m=[1,2,2,3,4,5,6,7,6,5,7,8]
# n=[3,4,1,2,3,47,8]
# def hasing(m,n):
#     dic={}
#     for i in m:
#         dic[i]=dic.get(i,0)+1
    
#     for i in n:
#         if i in dic:
#             print(i,"-->",dic[i])
#         else:
#             print(i,"-->",0)

        
# hasing(m,n)


# Charater Frequency Counting using Hashing

# s="tejasshindeededed"
# a="tsinedf"

# def c_hasing(s,a):
#     dic={}
#     for i in s:
#         dic[i]=dic.get(i,0)+1
    
#     for i in a:
#         if i in dic:
#             print(i,dic[i])
#         else:
#             print(i,0)

# c_hasing(s,a)



# recursions


# factorial number .................
# n=5

# def num_fact(n):
#     if n<=0:
#         return 1
#     return n*num_fact(n-1)

# print(num_fact(n))


# fibbonaci series..................

# fibbo=11

# def fibbo_series(n):
#     if n <=1:
#         return n
#     return fibbo_series(n-1)+fibbo_series(n-2)

# print(fibbo_series(fibbo))
    
# print the number of this four times

# cnt=0
# def func(cnt):
#     if cnt==4:
#         return
#     print("anirudh")
#     cnt+=1
#     func(cnt)

# func(cnt)


# print 1 to n

# n=int(input("enter the number..."))

# def fucn(n):
#     if n==0:
#         return
#     fucn(n-1)
#     print(n)

# fucn(n)

# print n to 1

# n=8
# def func(n):
#     if n==0:
#         return
#     print(n)
#     func(n-1)
# func(n)

# sum of first n numbers 

# n=6

# def func(n):
#     if n==0:
#         return 0
#     return n + func(n-1)
# print(func(n))