# 1. Practice Problem: Move Zeroes
# The Goal: Given an integer array nums, 
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Constraint: You must do this in-place without making a copy of the array.
# The Logic Tool: Fast & Slow Pointers (Reader/Writer).
# Example 1:
# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# Hint: Use a variable write_index starting at 0. 
# Loop through the array with read_index. If nums[read_index] is not 0, 
# put it at nums[write_index] and move write_index forward. 
# (Don't forget to fill the remaining spots with zeros if your logic doesn't swap automatically!)

# nums = [0, 1, 0, 3, 13]
# def move_zeroes(nums):
#     wr = 0 # Writer (Slow Pointer)
#     # Start from 0, check EVERY number
#     for rr in range(len(nums)): 
#         # LOGIC FIX: Check if the value is NOT ZERO
#         if nums[rr] != 0:
#             # ACTION FIX: Swap them (so we don't lose the zero)
#             nums[wr], nums[rr] = nums[rr], nums[wr]
#             wr += 1
#     print(nums)
# move_zeroes(nums)







# 2. Practice Problem: Valid Anagram
# The Goal: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Definition: An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#  typically using all the original letters exactly once.
# The Logic Tool: Frequency Map (Dictionary/Hash Map).
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Hint: Create a dictionary. Loop through s and add 1 for every character. 
# Loop through t and subtract 1 for every character (or check if the counts match). 
# If the final dictionary counts are all zero (or if the two dictionaries are equal), it is a match.
# s='anagram'
# t='nagaram'

# def anagram(s,t):
#     sd={}
#     td={}
#     if len(s)!=len(t):
#         return False
    
#     for i in s:
#         print(i)
#         if i not in sd:
#             sd[i]=1
#         else:
#             sd[i]+=1
#     for i in t:
#         if i not in td:
#             td[i]=1
#         else:
#             td[i]+=1
#     if sd==td:
#         return True
#     else:
#         return False
# print(anagram(s,t))










# 3. Practice Problem: Two Sum II - Input Array Is Sorted
# The Goal: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

# Return: The indices of the two numbers, added by 1 (1-based index).

# The Logic Tool: Two Pointers (Opposite Ends).

# Example 1:

# Input: numbers = [2, 7, 11, 15], target = 9

# Output: [1, 2]

# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

# Example 2:

# Input: numbers = [2, 3, 4], target = 6

# Output: [1, 3]

# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.

# Hint: Start left at 0 and right at the last index. Calculate sum. If sum > target, decrement right.
#  If sum < target, increment left. Remember to add +1 to your final answer indices!

# num=[2,7,11,15,20]
# tg=17
# def twosum(num,tg):
#     lp=0
#     rp=len(num)-1
#     while lp<rp:
#         sum=num[lp]+num[rp]
#         if sum==tg:
#             print("theae tow positions are the :",lp+1,"##",rp+1)
#             break
#         elif sum>tg:
#             rp-=1
#         elif sum<tg:
#             lp+=1

# twosum(num,tg)




# 🚀 New Logic Unlocked: The Sliding Window

# sliding window techniques......
# max sum of the sub array and window is w=3

# n=[6,9,9,2,4,5,7,8]
# w=4

# cursum=0
# for i in range(len(n)):
#     if i<w:
#         cursum+=n[i]
#     else:
#         break
# max=cursum
# for i in range(1,len(n)-w+1):
#     cursum=cursum-n[i-1]+n[i+w-1]
#     if cursum>max:
#         max=cursum
#     else:
#         pass
# print("maximum sum of the array is ",max) 