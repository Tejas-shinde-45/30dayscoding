# # most frequent elements


# a=[2,3,3,4,5,3,4,2,3]
# dic={}
# for i in a:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# maxi=0
# element=None
# for k,v in dic.items():
#     if v>maxi:
#         maxi=v
#         element=k
# print(maxi,element)

# lst=[2,3,3,4,5,3,4,2,3]
# most_frequent = max(set(lst), key=lst.count)
# print(most_frequent)

# another way 

# a=[2,3,3,4,5,3,4,2,3]
# dic={}
# n=len(a)
# for i in range(n):
#     dic[a[i]]=dic.get(a[i],0)+1

# print(dic)

# finding the even and odd from the array........

# a=[12, 7, 19, 24, 31, 42, 55]
# even=[]
# odd=[]
# for i in a:
#     if i % 2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even,odd)

# dictionaries sorting based on the valueas and keys


# sorted_freq={}
# dic={ 4: 2,5: 3,7: 2, 6: 2,  8: 1}

# for key in sorted(dic,key=dic.get):
#     sorted_freq[key] = dic[key]

# print(sorted_freq)


# mounted array quenstions........



# a=[7,9,10,11,15,5,4]

# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         pass
#     else:
#         print(a[i])
#         break


# finding the missing value from the arrray...

# arr=[1,2,3,4,5,7]
# def ms(arr):
#     n=len(arr)
#     current_sum=sum(arr)
#     expected_sum=n*(n+1)//2
#     element=expected_sum-current_sum

#     return element

# a=ms(arr)
# print(a)

