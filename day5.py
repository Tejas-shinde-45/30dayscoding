# Day 5 – Searching & Sorting
# Focus: Basic algorithms
# Questions: 
# 1. Linear search 
# lis=[4,3,1,7,8]
# target=7
# def lin_ser(lis,tg):
#     for i in range(len(lis)-1):
#         if lis[i] == tg:
#             print(f"target is found at this position.{i}")
#         else:
#             pass
# lin_ser(lis,target)

# 2. Binary search 
# lis=[10,11,12,13,14,15,16,17,18]
# tg=16
# def bi_serch(lis,tg):
#     st=0
#     end=len(lis)-1
    
#     while st<=end:
#         mid= (st+end)//2
#         if lis[mid]==tg:
#             print("found herer ",mid,lis[mid])
#             break
#         else:
#             st=mid
#             end=len(lis)-1
#             mid=(st+end)//2
# bi_serch(lis,tg)

# 3. Bubble sort 

# n=[3,4,5,2,1,9,6]
# def bubble_sort(n):
#     for i in range(len(n)-1):
#         # print(i)
#         for j in range(0,len(n)-1-i):
#             # print(j)
#             if n[j]>n[j+1]:
#                 n[j],n[j+1]=n[j+1],n[j]
#             else:
#                 pass
#         print("-----------------------------------")
#         print(n)
#     print(n)
# bubble_sort(n)


# 4. Insertion sort 

# n=[3,4,5,2,1,9,6]
# def insertion_sort(n):
#     for i in range(1,len(n)):
#         key=n[i]
#         j=i-1
#         while j>=0 and n[j]>key:
#             n[j+1]=n[j]
#             j-=1
#         n[j+1]=key
#     print(n)
# insertion_sort(n)

# 5. Selection sort
# arr=[3,4,5,2,1,9,6]
# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         min_index = i  # assume the first element is smallest

#         # find the actual smallest element in the remaining array
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         # swap only if needed
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr


# print(selection_sort(arr))

# 🎯 Daily Challenge: Sort a list without using sort() or sorted().

# i have used the insertion sort....
# li=[66,44,22,11,88,38]

# def insertion_sort(li):
#     for i in range(1,len(li)):
#         key=li[i]
#         j=i-1
#         while j>=0 and li[j]>key:
#             li[j+1]=li[j]
#             j-=1
#         li[j+1]=key
#     print(li)
# insertion_sort(li)
