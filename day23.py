# def prime(n):
#     for i in range(2,int(n//2)):
#         if n%i==0:
#             print("not prime")
#             break
#     print("prime")

# prime(8)

# 

# a=[1,2,3,7,8]
# t=4

# def two_sum(a,t):
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]+a[j]==t:
#                 print("target is got",a[i],a[j])

# two_sum(a,t)


# a=[1,3,4]
# b=a
# a.append(5)
# print(b)

# for i in range(1, 21):
#     if i % 15 ==0:  # Check BOTH first
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# a=[i**2 for i in range(5)]
# print(a)

# names = ["Alice", "Bob", "Amber", "Charlie", "Anna"]

# new=[i for i in names if i[0]=="A"]
# print(new)


# a=['tejas','aa ',' dipak  ',' abc']
# r_cnt=0
# def clean_data(a):
#     global r_cnt
#     clean=[]
#     for i in a:

#         clean_i=i.strip()
#         if len(clean_i)>3:
#             clean.append(clean_i)
#         else:
#             r_cnt+=1
#     print(clean)

# clean_data(a)




# reverse printing.........
        
# a=2345
# while a>0:
#     digit = a%10
#     print(digit)
#     a=a//10

#  sum of given numbers 

# a=2345
# sum=0
# while a>0:
#     digit = a%10
#     sum+=digit
#     a=a//10
# print(sum)

# number reversing......first approach
# a=2345
# rev=""
# while a>0:
#     digit = a%10
#     rev+=str(digit)
#     a=a//10

# print(int(rev))

# number reversersing.... best approch second
# a=12345
# rev=0
# while a>0:
#     digit=a%10
#     rev=rev*10 + digit
#     a=a//10
# print(rev)

#  sum of the even elements fromt this value
# a=1234567
# sum=0
# while a>0:
#     digit=a%10
#     if digit % 2==0:
#         sum+=digit
#     a=a//10
# print(sum)

# 