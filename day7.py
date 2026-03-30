# Day 7 – Recursion Problems
# Focus: Recursive logic & thinking
# Questions: 
# 1. Factorial using recursion
# 
# targ=4
# def fact(t):
#     if t<=0:
#         return 1
#     return t*fact(t-1)
# print(fact(targ))

#  2. Fibonacci using recursion 
# def fibbo(t=11):
#     if t<=1:
#         return t
#     return fibbo(t-1) + fibbo(t-2)
# print(fibbo())

# 3. Sum of digits using recursion
# d=324
# def sumof(d):
#     if d<=0:
#         return d
#     return (d%10)+sumof(d//10)
# print(sumof(d))

#  4. Reverse string using recursion 
# d='tejas'
# def rev(d):
#     if d=="":
#         return ""
#     return rev(d[1:])+d[0]
# print(rev(d))

# 5. GCD of two numbers using recursion

# 🎯 Daily Challenge: Print all numbers from 1 to N using recursion.
# print([[i+j for i in "abc"] for j in "def"])
