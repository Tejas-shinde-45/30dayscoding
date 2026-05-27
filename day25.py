# Find Largest Element
# a=[2,3,4,5,6,4,3]
# max=0
# for i in a:
#     if i > max:
#         max=i
# print(max)
# Find Second Largest Element

# a=[2,3,4,5,6,4,3]
# max=0
# smax=0
# for i in a:
#     if i > max:
#         smax=max
#         max=i
#     elif i >smax and i != max:
#         smax=max
#         max=i

# print(smax)


# “Check if array is sorted”

# a=[1,3,9]
# flag=True
# for i in range(len(a)-1):
#     if a[i] > a[i+1]:
#         flag=False
#         break
# print(flag)


# Reverse an Array

# a=[2,3,4,5]
# l=0
# r=len(a)-1
# while l<r:
#     a[l],a[r]=a[r],a[l]
#     l+=1
#     r-=1
# print(a)

# move zeros

# a=[0,1,0,3,12]
# l=0
# r=0
# while l<len(a):
#     if a[l]==0:
#         l+=1
#     elif a[l]!=0:
#         a[r],a[l]=a[l],a[r]
#         r+=1
#         l+=1
# print(a)

# Remove Duplicates From Sorted Array

# a=[1,1,2,2,3,4,4]

# u=0

# for i in range(1,len(a)):

#     if a[i] != a[u]:

#         u+=1
#         a[u]=a[i]

# print(a[:u+1])


