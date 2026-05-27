# star pattern
# n=5
# for i in range(1,n+1):
#     print("*"*i)

# output
# *
# **
# ***
# ****
# *****

# star pattern
# n=5
# for i in range(n+1):
#     print("*" *(n-i))

# output
# *****
# ****
# ***
# **
# *


# n=5

# for i in range(n):

# # Assuming EVERY month has 30 days
# y = int(input("Year: "))
# m = int(input("Month: "))
# d = int(input("Day: "))

# # Add 3 days
# d = d + 3

# # Check for Month Rollover
# if d > 30:
#     d = d - 30
#     m = m + 1

# # Check for Year Rollover
# if m > 12:
#     m = 1
#     y = y + 1

# print(f"Result: {y}-{m:02d}-{d:02d}")

# =========================

# s='property'
# lis=list(s)
# lis2=[]
# for i in lis:
#     if i in lis2:
#         pass
#     else:
#         lis2.append(i)
# s2="".join(lis2)
# print(s2)


# =====================================

# n=5

# for i in range(1,n+1):
#     print(" "*(n-i),'*'*(i))

#      *
#     **
#    ***
#   ****
#  *****
# =======================================

# n=5

# for i in range(1,n+1):
#     print("*"* i,end=" ")

# # diamond star pattern...................
# n=5

# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))

# for i in range(1,n+1):
#     print(" "*i+"*"*(2*(n-i)-1))

# ..........................................

# first non reapeting element from the string..

# c="aabbwcdde"
# dic={}

# for i in c:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# for i,v in dic.items():
#     if v==1:
#         print(i,":",v)
#         break

# ================================================

# a=[2,3,4,8,7,9,5,4]

# max=0
# smax=0
# for i in a:
#     if i>max:
#         smax=max
#         max=i
# print(max,smax)

# ======================================

# a="abccbdeadbedldeolsde"
# def longest_unique_substring(s):
#     char_set = set()
#     left = 0
#     max_len = 0

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1

#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)

#     return max_len

# print(longest_unique_substring(a))


# printing logest substring

# def longest_substring(s):
#     char_set = set()
#     left = 0
#     max_length = 0
#     longest_sub = ""

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1

#         char_set.add(s[right])

#         if right - left + 1 > max_length:
#             max_length = right - left + 1
#             longest_sub = s[left:right+1]

#     return max_length, longest_sub


# s = "abcabcbb"
# length, substring = longest_substring(s)

# print("Length:", length)
# print("Substring:", substring)


# printing the sub string
# s='heywhy'
# def substring(s):
#     for i in range(len(s)):
#         for j in range(i,len(s)):
#             print(s[i:j+1],end=",")

# substring(s)

