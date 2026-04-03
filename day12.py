
# Input: nums = [1,2,3,4,5,6,7,8], k = 4

# Output: [5,6,7,8,1,2,3,4]

# 🚀 New Logic Unlocked: The Sliding Window

# sliding window techniques......

# arr=[2, 1, 5, 1, 3, 2]
# w=3

# curr=0
# for i in range(len(arr)):
#     if i<w:
#         curr+=arr[i]
#     else:
#         break

# maxx=curr
# for i in range(1,len(arr)-w+1):
#     curr=curr-arr[i-1]+arr[i+w-1]
#     if maxx<curr:
#         maxx=curr
#     else:
#         pass
# print(maxx)



# finding the logest substring couts...

# s = "abcabcbb"
# def logestsub(s):
#     l=0
#     a=set()
#     max_cnt=0
#     for r in range(len(s)):
#         while s[r] in a:
#             a.remove(s[l])
#             l+=1

#         a.add(s[r])

#         max_cnt=max(max_cnt,r-l+1)

#     return max_cnt
# print(logestsub(s))

s = "abcabcbb"
def longestsub(s):
    l = 0
    a = set()
    max_cnt = 0
    # 1. EXPAND (Right Pointer moves)
    for r in range(len(s)):
        # 2. SHRINK (Left Pointer moves)
        # We only shrink WHILE the duplicate exists in the set
        while s[r] in a:
            a.remove(s[l]) # Remove the character on the far left
            l += 1         # Move the left pointer forward
        # 3. UPDATE (Now it's safe to add)
        a.add(s[r])
        
        # 4. MEASURE
        # Current window size is (right - left + 1)
        max_cnt = max(max_cnt, r - l + 1)
        
    return max_cnt

print(longestsub(s))




# t=[2,3,4,5,6,7,2,3,1]
# w=2

# def tp(t,w):
#     curr=0
#     for i in range(len(t)):
#         if i<w:
#             curr+=t[i]
#         else:
#             break
#     maxx=curr
#     for i in range(1,len(t)-w+1):
#         curr=curr-t[i-1]+t[i+w-1]
#         if maxx<curr:
#             maxx=curr
#         else:
#             pass
#     print(maxx)
# tp(t,w)
