# li=[2,2,4,4,5,6,7,7,8,9]
# count={}
# for i in li:
#     count[i]=count.get(i,0)+1
# print(count)



# li=[2,2,4,4,5,6,7,7,8,9]

# for index,value in enumerate(li):
#     print(index,value)
#     if index==4:
#         print("here is my boy")


# slow fast pointers
# a=[0,3,0,4,0,2,1]
# def fast_slow(a):
#     wr=0
#     for rr in range(len(a)):
#         if a[rr] !=0:
#             a[wr],a[rr]= a[rr],a[wr]
#             wr+=1
#     print(a)
# fast_slow(a)

# reverse not using the two pointwes
# string='tejas'
# def reverse(s):
#     w=len(string)-1
#     rev=""
#     while 0<=w:
#         rev+=s[w]
#         w-=1

#     print(rev)

# reverse(string)


# reverse using the two pointers

# a='tejas'
# def reverse(a):
#     l=0
#     a=list(a)
#     w=len(a)-1
#     while l<w:
#         a[l],a[w]=a[w],a[l]
#         l+=1
#         w-=1

#     return "".join(a)

# print(reverse(a))


# # armstrong numbers

# n=int(input("enter the numebr"))
# num=n
# # n=int(input("enter the numebr"))
# power=len(str(n))
# sum=0

# while n>0:
#     digit=n%10
#     sum+=digit ** power
#     n=n//10
# if sum == num:
#     print(num,"armstrong")
# else:
#     print(num,"its not armstrong")


# another method of finding armstrongs 
# n=input("enter the number")
# num=n
# power=len(str(n))
# sum1=0
# for i in n:
#     sum1+=int(i)**power
# print(sum1)


# evan number of till the 100
# cnt=0
# for i in range(101):
#     if i % 2 ==0:
#         print(i)
#         cnt+=1
#     else:
#         pass

# print(cnt)


#vowels count 

# s="tejasshinde"

# def vowels(s):
#     vcnt=0
#     ccnt=0
#     v='aeiou'
#     for i in s:
#         if i.lower() in v:
#             vcnt+=1
#         else:
#             ccnt+=1
#     print(vcnt,ccnt)
# vowels(s)

# # string palinedrome
# a='madam'
# b=a[::-1]
# if a==b:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

# number palindrome
# n=1234
# a=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev * 10 + digit
#     n=n//10
# print(a,rev)

# reverse number 
# a=4561
# rev=0
# while a>0:
#     digit=a%10
#     rev=rev * 10 +digit
#     a=a//10
# print(rev)

# armstrog
# a=153
# n=a
# power=len(str(a))
# num=0
# while a>0:
#     digit=a%10
#     num+=digit**power
#     a=a//10
# print(num)




# fibonaci series

# n=int(input("enter terms:"))
# a,b=0,1
# for i in range(n):
#     print(a,end="")
#     a,b=b,a+b


# prime or not

# n=int(input("enter the number:"))
# if n<=1:
#     print("number is not prime")
# else:

#     for i in range(2,n//2+1):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#             print("prime")


# n = int(input("Enter number: "))

# if n <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

# duplicate counting.......
# a=[1,2,3,4,5,64,4,3,1,2]
# b=[]
# dcnt=0
# for i in a:
#     if i in b:
#         dcnt+=1
#     else:
#         b.append(i)
# print(dcnt,b)

# sorting
b=[4,3,2,5,1,7]
 
# for i in range(len(b)):
#     for j in range(i,len(b)):
#         if b[i]>b[j]:
#             b[i],b[j]=b[j],b[i]
# print(b)


# for i in b:
#     print(i)

# for i in range(len(b)-1):
#     print(b[i])


