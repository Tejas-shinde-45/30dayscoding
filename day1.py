# Day 1 – Basics & Patterns

# Focus: Loops, conditions, and basic math logic
# Questions: 

# 1. Check if a number is even or odd 
# n=int(input("enter the number:"))
# def eo(m):
#     if m % 2==0:
#         print(f"number is even:-{m}")
#     else:
#         print(f"number is odd:-{m}")
# eo(n)


# 2. Find max of three numbers
# l1=[1,4,2]
# def maxnumber(l1):
#     m=0
#     for i in l1:
#         if i>m:
#             m=i
#     print(m)
# maxnumber(l1) 

#  3. Sum of digits of a number 
# method one.
# n=2312
# sumof=0
# while n>0:
#     sumof+=n%10
#     n//=10
# print(sumof)

# 4. Print multiplication table 
# n=5
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)


# 5. Print star patterns (triangle, pyramid)
# n=5
# for i in range(6):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# 🎯 Daily Challenge: Create a half pyramid using numbers or stars.

n=6
for i in range(6):
    for j in range(i+1):
        print("*",end="")
    print()