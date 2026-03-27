# Day 2 – Number Logic
# Focus: Prime, factorial, Fibonacci, palindrome
# Questions:

#  1. Check if a number is prime 
# n=5
# def primeornot(n):
#     if n<=1:
#         return False
#     for i in range(2,n//2):
#         if n % i==0:
#             return False
#     return True
# if primeornot(n):
#     print("number is prime....")
# else:
#     print("number is not prime..")


# 2. Find factorial of a number 
# The factorial of a number is the product of all integers from 1 to that number. For example, the factorial of 5 (written as 5!) is 1∗2∗3∗4∗5=120.
# def factorial(n):
#     fact=1
#     if n>=1:
#         for i in range(1,n+1):
#             fact=fact*i
#             print(fact)
#     return fact
# print(factorial(5))


# 3. Print Fibonacci sequence 
# The Fibonacci sequence is a series of numbers where each number is the sum of the two previous numbers,
#  starting from 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, ...
# def fibo(cnt):
#     a,b=0,1
#     if cnt<=1:
#         print("please enter the positive number.")
#     elif cnt==1:
#         print(a)
#     else:
#         for i in range(cnt):
#             print(a,end=" ")
#             a,b=b,a+b
#         print()
# fibo(6)
#
# 4. Check palindrome number 
#def palindrome(num):
#     original_num=num
#     reverse=0
#     while num>0:
#         digit=num % 10
#         print("digit",digit)
#         reverse=reverse % 10 +digit
#         print("reverse",reverse)
#         num //=10
#         print("num",num)
#     return original_num == reverse
# if palindrome(121):
#     print("number is palimdrome")
# else:
#     print("number is palimdrome")
#---------------------------------------------------------
# n = input("Enter a number: ")

# if n == n[::-1]:
#     print("Palindrome ")
# else:
#     print("Not a Palindrome")



# 5. Check Armstrong number

# def armstrong(num):
#     original_num=num
#     sumof=0
#     while num>0:
#         digit=num % 10  #get last digit
#         sumof+=digit ** 3 # sumof=sumof + digit cubed
#         num//=10   # floor division to remove last digit 
        
#     return original_num==sumof

# if armstrong(153):
#     print("number is armstrong")
# else:
#     print("number is not armstrong")

# 🎯 Daily Challenge: Print all prime numbers between 1 and 100

# n=100
# for i in range(1,n+1):
#     if i<=1:
#         pass
#     elif i==2:
#         print(i)
#     elif i>2:
#         for j in range(2,i):
#             if i % j==0:
#                 break
#             else:
#                 print(i)
#                 break

# n = 100
# print(f"Prime numbers between 1 and {n}:")

# for num in range(1, n + 1):
#     # Prime numbers must be greater than 1
#     if num > 1:
#         # Check for factors
#         # We check from 2 up to (num - 1)
#         for i in range(2, num):
#             if (num % i) == 0:
#                 # Found a factor, not prime
#                 # Break out of the inner loop
#                 break
#         else:
#             # This 'else' belongs to the 'for' loop
#             # It only runs if the loop completed without a 'break'
#             # Meaning, no factors were found.
#             print(num)

