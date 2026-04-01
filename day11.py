# First Unique Character
# s='leetcodel'
# dic={}

# def uni(s,dic):
#     cnt=0
#     for i in s:
#         if i not in dic:
#             dic[i]=cnt+1
#         elif i in dic:
#             dic[i]+=1
    
#     for i,v in enumerate(s):
#         if dic[v]==1:
#             return i
    
#     return -1

# print(uni(s,dic))

#Find the number that appears only once.
# nums=[4,2,1,2,1,4,6]
# def oo(num):
#     di={}
#     for i in num:
#         if i not in di:
#             di[i]=1
#         elif i in di:
#             di[i]+=1
#     print(di)
#     # for i ,v in enumerate(nums):
#     #     if di[v] == 1:
#     #         return nums[i]/
#     for key in di:
#         if di[key]==1:
#             return key
# print(oo(nums))

#find string is anagram or not

# a="tejas"
# b="saj et"

# def can(a,b):
#     l1=[]
#     l2=[]
#     for i in a:
#         l1.append(i)
#     for i in b:
#         l2.append(i)
#     if sorted(l1)==sorted(l2):
#         return True
#     else:
#         return False
    
# print(can(a,b))
#second method....................................................
# def isAnagram(s, t):
#     # Quick check: if lengths differ, they can't be anagrams
#     if len(s) != len(t):
#         return False

#     count_s = {}
#     count_t = {}

#     # Count frequency of s
#     for char in s:
#         count_s[char] = count_s.get(char, 0) + 1

#     # Count frequency of t
#     for char in t:
#         count_t[char] = count_t.get(char, 0) + 1

#     # Compare the two dictionaries directly
#     print(count_s,count_t)
#     return count_s == count_t

# # Test
# print(isAnagram("elisten", "sielent")) # True
# print(isAnagram("rat", "car"))       # False

#using modules collection ............................
# from collections import Counter

# def isAnagram(s, t):
#     return Counter(s) == Counter(t)
# print(isAnagram('tejas','makes'))


#palindrome using the two pointer 
# s="matdtam"
# left=0
# right=len(s)-1
# flag=True
# while left<right:
#     if s[left]!=s[right]:
#         print("String is not lindrom")
#         flag=False
#         break
    
#     left+=1
#     right -=1

# if flag:    
#     print("string is plindrome...")
    
# list reversing 

# li=['t','e','j','a','s']
# l=0
# r=len(li)-1
# while l<r:
#     li[l],li[r]=li[r],li[l]
#     l+=1
#     r-=1
# print(li)

#push zeros at the ending of the list 
# input=[1,0,4,3,0,2]
# ouput=[1,4,3,2,0,0]

# i=[1,0,4,3,0,2]
# def pz(i):
#     w=0
#     for r in range(0,len(i)):
#         if i[r] != 0:
#             i[r],i[w]=i[w],i[r]
#             w+=1
#     print(i)
# pz(i)


# another one ........
# nums = [0, 0, 1, 1, 1, 3, 3, 3]

# def point(nums):
#     w=1
#     for r in range(1,len(nums)):
#         if nums[r]!=nums[r-1]:
#             nums[w]=nums[r]
#             w+=1
#     print(nums)

# point(nums)

# finding sum of two indexes

# a=[2,7,11,15,23]

# target=22
# r=0
# for w in range(len(a)-1,0,-1):
#     if a[r]+a[w]==target:
#         print(r,w,"these indexes combinations is comming our targest values...")
#     else:
#         r+=1



# a=[2,7,11,15,23]
# tg=22
# l=0
# r=len(a)-1
# while l<r:
#     csum=a[l]+a[r]
    
#     if tg==csum:
#         print("we find the sum on this positions..",l+1,r+1)
#         break
#     elif csum<tg:
#         l+=1
#     else:
#         r-=1



