# check number is palindrome or not

# num=121

# def pali(num):
#     reverse=0
#     ori=num

#     while num>0:
#         digit= num%10
#         print(digit)
#         reverse=reverse * 10 + digit
#         print(reverse)
#         num//=10
#         print(num)
    
#     if ori==reverse:
#         return True
#     else:
#         return False

# print(pali(num))

# find the second max number from the list.
# a=[-11,-22,-33,44]
# max=float('-inf')
# smax=float('-inf')
# for i in a:
#     if i>max:
#         smax=max
#         max=i
#     elif i>smax and i!=max:
#         smax=i
# print(smax,max)

# find the missing number in array

# a=[1,2,3,5]

# n=len(a)+1
# expected=n*(n+1)//2
# actual_sum=sum(a)

# missing=expected - actual_sum
# print("missing number:",missing)

# find duplicate elemetn in list

# a=[1,2,3,2,4,1]
# uni=[]
# for i in a:
#     if i in uni:
#         print(i)
#     else:
#         uni.append(i)


# 👉 Find first non-repeating character

# s="aabbcdd"
# lis=list(s)
# print(lis)

# def nonreapiting(lis,s):
#     cnt={}
#     for i in lis:
#         if i in cnt:
#             cnt[i]+=1
#         else:
#             cnt[i]=1
#     print(cnt)
#     for a,v in enumerate(s):
#         if cnt[v]==1:
#             print(a,v)
# nonreapiting(lis,s)

# shifr all zero last
# l=[0,1,0,3,12]
# s=0
# for f in range(len(l)):
#     if l[f]!=0:
#         l[s],l[f]=l[f],l[s]
#         s+=1
# print(l)
        

# maximum sum of contineuos sub array

# nums = [2,1,3,4,1,2,1,5,4]
# current_sum = 0
# max_sum = 0
# for i in nums:
#     current_sum = max(i, current_sum + i)
#     max_sum = max(max_sum, current_sum)
# print(max_sum)