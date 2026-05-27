# 📝 The Core Logic Test
# Q1: The Toll Booth (Loops & Conditionals)
# You are given a list of random numbers: [4, 7, 2, 9, 5, 8]
# Write the logic to find the sum of ONLY the odd numbers in that list.

# a= [4, 7, 2, 9, 5, 8]
# odsum=0
# for i in a:
#     if i % 2 == 0:
#         pass
#     else:
#         odsum+=i
# print(odsum)



# Q2: King of the Hill (Variables & State)
# You are given an unsorted list of numbers: [12, 4, 56, 17, 8, 99, 23]
# Write the logic to find the absolute biggest number in this list without using the max() function. (Imagine you are looking at them one by one).
# b= [12, 4, 56, 17, 8, 99, 23]
# maxa=0
# for i in b:
#     if i > maxa:
#         maxa=i
# print(maxa)
# Q3: The Mirror (Strings & Pointers)
# You are given a word as a string, like "racecar" or "apple".
# Write the logic to check if the word is a Palindrome (spelled the exact same forwards and backwards). Again, no built-in reverse shortcuts allowed!

# s="racefcar"
# o=s
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

# if o==rev:
#     print("string is palimdrome")
# else:
#     print("string is not")


# ====================\

# s='tejas'
# l=list(s)
# lp=0
# rp=len(l)-1
# while lp<rp:
#     l[lp],l[rp]=l[rp],l[lp]
#     lp+=1
#     rp-=1

# b="".join(l)
# print(s,b)

