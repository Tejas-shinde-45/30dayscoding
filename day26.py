
# Best Time to Buy and Sell Stock
# a=[7,1,5,3,6,4]
# min_price=a[0]
# max_profit=0

# for i in a:

#     if i<min_price:
#         min_price=i
    
#     profit=i-min_price

#     if profit > max_profit:
#         max_profit=profit

# print(max_profit)



# Two Sum
# a=[2,3,4,5,1,6,3,7,8]

# t=12

# def two_sum(t,a):
    # na=sorted(a)
    # print(na)

    # n=len(a)
    # for i in range(n):
    #     for j in range(i,n-1):
    #         if a[i]>a[j]:
    #             a[i],a[j]=a[j],a[i]
    
#     r=len(a)-1
#     l=0
#     while l<r:
#         sumtwo= a[l]+a[r]
#         if sumtwo==t:
#             print(l,r,"this is the index we get the array")
#             break
#         elif sumtwo>t:
#             r-=1
#         else:
#             l+=1

# two_sum(t,a)


# a = [1,2,3,4,5,6,7,8]
# t = 9

# l = 0
# r = len(a)-1

# while l < r:

#     total = a[l] + a[r]

#     if total == t:
#         print(l, r)
#         break

#     elif total > t:
#         r -= 1

#     else:
#         l += 1



# a = [2,3,4,5,1,6,3,7,8]
# target = 9

# seen = {}

# for i in range(len(a)):

#     complement = target - a[i]

#     if complement in seen:
#         print(seen[complement], i)

#     seen[a[i]] = i
# print(seen)





a = [2,3,4,5,1,6,3,7,8]
target = 9

dic={}
for i in range(len(a)):

    c=target-a[i]
    if c in dic:
        print(dic[c],i)
    dic[a[i]]=i



