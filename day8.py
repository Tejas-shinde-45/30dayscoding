# Day 8 – Logical & Puzzle Type
# Focus: Brain teasers & common interview puzzles
# Questions: 
# 1. Find missing number in list 
# lis=[1,2,4,5]
# def misin(lis,n):
#     total_sum=n*(n+1)//2
#     return total_sum-(sum(lis))
# print("missing value is :",misin(lis,5))

# 2. Find duplicates in list 

# lis=[1,2,3,4,5,3,4,3]

# def duplicates(lis):
#     lis1=[]
#     lis2=[]
#     for i in lis:
#         if i not in lis1:
#             lis1.append(i)
#         elif i not in lis2:
#             lis2.append(i)
        
#     print(lis1)
#     print(lis2)
# duplicates(lis)
# 8888888888888888888888888888888888888888888888888888888888888888888
# def duplicates(lis):
#     cnt=0
#     seen = set()
#     dup = set()
#     for x in lis:
#         if x in seen:
#             dup.add(x)
#         else:
#             seen.add(x)
#     print(list(seen))
#     print(list(dup))

#     for i in dup:33
#         cnt+=1
#     print(cnt)
# lis=[1,2,3,4,5,3,4,3]
# duplicates(lis)

# 3. Swap two numbers without using third variable 
# a=3
# b=5
# print(f"before swapping :a:{a},b:{b}")
# def swap(a,b):
#     a,b=b,a
#     print(f"after swapping :a:{a},b:{b}")
# swap(a,b)
# print(f"after swapping :a:{a},b:{b}")

# 4. Reverse words in a sentence 
# sen="tejas is my name"

# rev="  ".join(sen.split()[::-1])
# print(rev)


# 5. Check if two strings are anagrams

# s1="silent"
# s2="listen"
# def are_anagrams_sort(s1, s2):
#     return sorted(s1) == sorted(s2)
# print(are_anagrams_sort(s1,s2))

# 🎯 Daily Challenge: Find first non-repeated character in a string.

