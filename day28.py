# Basic DSA..........

#  Extraction of digit or numbers..........

# -Count of digits
# num=23432
# n=num
# cnt=0
# while n>0:
#     digit=n%10
#     cnt+=1
#     n=n//10
# print(cnt)

# using lograthmic method

#  the point is that when you find the 
# log10 of a number and add 1 to that then it gives you count of the digits this is a trick and this is a trick

# Reverse a number
# m=num
# rev=0
# while m>0:
#     digit=m%10
#     rev=rev*10 +digit
#     m=m//10
# print(rev)

# Check palindrome or not
# p=num
# rev=0
# while p>0:
#     last_digit=p%10
#     rev=rev*10+last_digit
#     p=p//10

# if rev==num:
#     print("number is palindrome")
# else:
#     print("number is not")

# Armstrong number
# num1=153
# a=num1
# b=num1
# cnt=0
# sum=0
# while b>0:
#     if a>0:
#         last_digit=a%10
#         cnt+=1
#         a=a//10
#     else:
#         l_d=b%10
#         sum+=l_d**cnt
#         b=b//10
# if num1==sum:
#     print("numeber is armstrong")
# else:
#     print("number is not")

# print all factor of a given numbers

# num=20
# for i in range(1,num+1):
#     if 20 % i==0:
#         print(i,end=",")


# another method


# num=36
# from math import sqrt
# result=[]
# for i in range(1,int(sqrt(num))+1):
#     if num%i==0:
#         result.append(i)
#         if num // i !=i:
#             result.append(num//i)
# print(result)

# store the frequency of the digits of numbers


# n=3456
# num=n
# while num>0:
#     last_digit=num%10
#     print(last_digit,end="")
#     num=num//10

