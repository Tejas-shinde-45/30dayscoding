# Day 3 – String Operations
# Focus: String reversal, frequency, and manipulation
# Questions: 1. Reverse a string 
# a='tejas'
# def reverse(a):
#     rev=''
#     for i in a:
#         rev=i+rev
#     print(rev)
# reverse(a)

# 2. Check if string is palindrome 
# def pali(a):
#     return a==a[::-1]
# print(pali('python'))
# print(pali('madam'))

# 3. Count vowels and consonants 
# def count(a):
#     v='aeiouAEIOU'
#     vc=cc=0
#     for i in a:
#         if i in v:
#             vc+=1
#         else:
#             cc+=1
#     print("vowels count is:",vc)
#     print("consonant count is:",cc)
# count("duplicatescharacter")

# 4. Remove duplicate characters 
# def dupl(a):
#     result=""
#     for i in a:
#         if i not in result:
#             result+=i
#     print(result)
# dupl('tejasshinde')

# 5. Find frequency of each character
# def freqq(a):
#     freq={}
#     for ch in a:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1

#     print(freq)
# freqq("tejastjeoskdowshinde")

# 🎯 Daily Challenge: Find the most frequent character in a string.

# def freqq(a):
#     freq={}
#     for ch in a:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1

#     print(freq)
#     max=0
#     maxc=''
#     for ch in freq:
#         if freq[ch]>max:
#             max=freq[ch]
#             maxc=ch
#     print(f"{maxc} this character is obtain {max} times..") 
# freqq("tejastjessoskdowshinde")