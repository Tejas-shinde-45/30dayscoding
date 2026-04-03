# binary search
# 
# num=[1, 3, 5, 6,10]
# target=2

# def binary_search(nums,target):
#     lb=0
#     ub=len(nums)-1

#     while lb<=ub:
#         mid=(lb+ub)//2
#         if nums[mid]==target:
#             return mid
#         else:
#             if nums[mid]<target:
#                 lb=mid+1
#             else:
#                 ub=mid-1
#     return lb

# print(binary_search(num,target))


# ar=[2,3,4,5,7,6,7,7,9]
# key=7

# def b_s(arr,k):
#     lb=0
#     up=len(arr)-1
#     ans=[]

#     while lb<=up:
#         mid=(lb+up)//2
#         if arr[mid]==k:
#             ans.append(mid)
#             lb = mid+1
#         else:
#             if arr[mid]<k:
#                 lb=mid+1
#             else:
#                 up=mid-1
            
#     print(ans)

# b_s(ar,key)


# # # find the last ones
# ar=[2,3,4,5,6,7,7,7,9]
# key=7

# def b_s(arr,k):
#     lb=0
#     up=len(arr)-1
#     ans=-1

#     while lb<=up:
#         mid=(lb+up)//2
#         if arr[mid]==k:
#             ans=mid
#             lb = mid+1
#         else:
#             if arr[mid]<k:
#                 lb=mid+1
#             else:
#                 up=mid-1
            
#     return ans

# print(b_s(ar,key))

# def b1_s(arr,k):
#     lb=0
#     up=len(arr)-1
#     ans=-1

#     while lb<=up:
#         mid=(lb+up)//2
#         if arr[mid]==k:
#             ans=mid
#             up = mid-1
#         else:
#             if arr[mid]<k:
#                 lb=mid+1
#             else:
#                 up=mid-1
            
#     return ans

# print(b1_s(ar,key))

# f_o=b1_s(ar,key)
# l_o=b_s(ar,key)
# ans=[]

# for i in range(f_o,l_o+1):
#     ans.append(i)
# print(ans)
    

# # # The Final Binary Search Challenge: "Count Occurrences"
# ar=[2,3,4,5,6,7,7,7,7,7,7,7,9]
# key=7
# def b_s(arr,k):
#     lb=0
#     up=len(arr)-1
#     ans=-1

#     while lb<=up:
#         mid=(lb+up)//2
#         if arr[mid]==k:
#             ans=mid
#             lb = mid+1
#         else:
#             if arr[mid]<k:
#                 lb=mid+1
#             else:
#                 up=mid-1
            
#     return ans
# def b1_s(arr,k):
#     lb=0
#     up=len(arr)-1
#     ans=-1

#     while lb<=up:
#         mid=(lb+up)//2
#         if arr[mid]==k:
#             ans=mid
#             up = mid-1
#         else:
#             if arr[mid]<k:
#                 lb=mid+1
#             else:
#                 up=mid-1
            
#     return ans

# f_o=b1_s(ar,key)
# l_o=b_s(ar,key)

# if f_o == -1:
#     print("Count is 0")
# else:
#     count = (l_o - f_o) + 1
#     print("Count is", count)

# ---------------------------------------------------------
# linear search 

# ar=[2,3,4,1,4,6,3,3]
# t=6
# def linear_search(ar,t):
#     for i in range(len(ar)):
#         if ar[i]==t:
#             print("target occure in this position",i+1)
# linear_search(ar,t)



# nums=[2,3,45,6,]
# for i ,v in enumerate(nums):
#     print(i,end="---")
#     print(v)


# first duplicate of the list.......................
nums=[2,2,3,3,3,5,5,4,1]
dic={}
def duplicate(nums,dic):
    for i in range(len(nums)):
        # if nums[i] in dic:
        #     dic[nums[i]]+=1
        # else:
        #     dic[nums[i]]=1
        dic[nums[i]]=dic.get(nums[i],0)+1
    for i,v in enumerate(nums):
        if dic[v]>2:
            return i

print(duplicate(nums,dic))

        


