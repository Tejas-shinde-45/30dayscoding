# # reverse using two pointers...
# # s='tejas'

# # r,l=0,len(s)-1
# # res=""
# # while r<=l:
# #     res+=s[l]
# #     l-=1

# # print(res)


# # mover zeros using the reader and writer method........

# a=[0,3,2,1,0,3,0,0]

# w=0
# for r in range(len(a)):
#     if a[r]!=0:
#         a[w],a[r]=a[r],a[w]

#         w+=1
# print(a)


# k=3 in [1, 2, 3, 4, 5,8,9,3]
# k=3
# l=[1, 2, 3, 4, 5,8,9,3]

# curr=sum(l[:k])
# print(curr)

# maxx=curr
# for i in range(k,len(l)):
#     curr+= l[i] - l[i-k]
#     maxx=max(maxx,curr)

# print(maxx)

# Search: Find the first and last position of 8 in [1, 8, 8, 8, 9].

# li=[1, 8, 8, 8, 9]
# p=8

# lb=0
# ub=len(li)-1

# while lb<=ub:
#     mid=(lb+ub)//2
#     if li[mid]==p:
#         print("target is got at this posision",mid)
#         ub=mid-1 for finding the first occurence 
#         lb=mid+1 for finding the second occurence
#     else:
#         if p<li[mid]:
#             ub=mid-1
#         else:
            # lb=mid+1


# recurssion... fact
# n=5

# def fact_find(n):
#     if n==1:
#         return 1
#     else:
#         return n* fact_find(n-1)

# print(fact_find(n))


# fibonacci number based on the number..

# f=17

# def fact_fin(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fact_fin(n-1) + fact_fin(n-2)

# print(fact_fin(f))

# Our dictionary to remember how many ways to climb 'n' stairs
# memo = {}

# def climbStairs(n):
#     # 1. Check Memory: Have we calculated this step before?
#     if n in memo:
#         return memo[n]
        
#     # 2. Base Cases (The Stop Signs)
#     if n == 1:
#         return 1  # 1 way to climb 1 stair (just take 1 step)
#     if n == 2:
#         return 2  # 2 ways to climb 2 stairs (1+1, or a single 2-step)
        
#     # 3. Recursive Step (Add the two previous steps together)
#     # We save the answer to the dictionary BEFORE returning it!
#     ans = climbStairs(n - 1) + climbStairs(n - 2)
#     memo[n] = ans
#     return ans

# # Let's test it for a big staircase!
# stairs = 10
# print("Ways to climb", stairs, "stairs:", climbStairs(stairs))