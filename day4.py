# Day 4 – Lists & Arrays
# Focus: Searching, max-min, duplicates, merge
# Questions: 
# 
# 1. Find max and min element 
# arr = [2, 3, 4, 5, 6, 1]

# def maxmin(arr):
#     min_val = arr[0]       # start with first element
#     max_val = arr[0]

#     for i in arr:
#         if i > max_val:
#             max_val = i
#         if i < min_val:
#             min_val = i

#     print("Max =", max_val)
#     print("Min =", min_val)

# maxmin(arr)


# 2. Remove duplicates from list 
# lis=[1,2,4,3,2,4,1]
# def rdu(lis):
#     lis1=[]
#     for i in lis:
#         if i in lis1:
#             pass
#         else:
#             lis1.append(i)
#     print(lis1)
# rdu(lis)

# 3. Find second largest element 
# lis2=[1,2,3,4,112,45]
# def slargest(lis):
#     sl=0
#     fl=0
#     for i in lis:
#         if i > fl:
#             sl=fl
#             fl=i
#         elif sl != fl and i>sl:
#             sl = i
#     print("second largest number:",sl)
# slargest(lis2)

# 4. Merge two sorted lists 

# ls1=[1,3,5]
# ls2=[2,4,6]

# def merge(a,b):

#     mrg=[]
#     i=0
#     j=0
#     while i< len(a) and j<len(b):
#         if a[i] < b[j]:
#             mrg.append(a[i]) 
#             i+=1
            
#         else:
#             mrg.append(b[j])
#             j+=1
#     print(mrg)
#     while i < len(a):
#         mrg.append(a[i])
#         i += 1

#     while j < len(a):
#         mrg.append(b[j])
#         j += 1
#     print(mrg)
# merge(ls1,ls2)

# 5. Reverse list without using built-in method
# lis=[2,3,4,1,3]
# lis1=[]
# for i in range(len(lis),0,-1):
#     lis1.append(lis[i-1])
# print(lis1)
    
# 🎯 Daily Challenge: Merge two lists and remove duplicates.
# a=[2,3,5]
# b=[6,5,4]

# mrg=[]
# i=0
# j=0
# while i< len(a) and j<len(b):
#         mrg.append(a[i]) 
#         i+=1
#         mrg.append(b[j])
#         j+=1
# print(set(mrg))

# **************************************

# a = [2, 3, 5]
# b = [6, 5, 4]

# merged = a + b          # merge the lists
# unique = list(set(merged))   # remove duplicates

# print(unique)


# *****************************************
# a = [2, 3, 5]
# b = [6, 5, 4]

# unique = list(set(a) | set(b))
# print(unique)
# 
