# Day 6 – Dictionaries & Tuples
# Focus: Key-value operations and logic
# Questions: 
# 1. Count frequency of elements in a list using dict 
# arr = [1,2,2,3,3,3,4,5,3]
# dic={}
# for i in arr:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)
    
# 2. Find key with maximum value 
# dic={'a':23,'b':55,'c':78,'d':12}
# max_key=''
# max_v=0
# for key,value in dic.items():
#     if value> max_v:
#         max_v=value
#         max_key=key
# print(max_key)

# 3. Swap keys and values 
# dic={'a':23,'b':55,'c':78,'d':12}
# dicn={}
# for key,value in dic.items():
#     dicn[value]=key
# print(dicn)

# 4. Combine two dictionaries 
# d1={'a':23,'b':55}
# d2={'c':78,'d':12}

# copy=d1.copy()
# copy.update(d2)
# print(copy)

# 5. Sort dictionary by value
# data = {"a": 3, "b": 1, "c": 2}

# items = list(data.items())
# sorted_dict = {}

# while items:
#     # step 1: assume first is smallest
#     min_pair = items[0]  # (key, value)
    
#     # step 2: find actual smallest
#     for pair in items:
#         if pair[1] < min_pair[1]:
#             min_pair = pair
    
#     # step 3: add to result
#     sorted_dict[min_pair[0]] = min_pair[1]
    
#     # step 4: remove from original list
#     items.remove(min_pair)

# print(sorted_dict)
# 🎯 Daily Challenge: Find common keys between two dictionaries.
