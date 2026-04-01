# Day 10 – Final Challenge Day 🎯
# Focus: Combine all concepts
# Mini Projects:
#  1. Calculator app 

# 2. Password strength checker 3. Simple quiz app 4. Word frequency analyzer 5. Number guessing game
# 🎯 Daily Challenge: Build a mini project that uses loops, lists, and functions together.


# pyramid in pythons

# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# n=5
# for i in range(n,0,-1):
#     print(i*"*",)

# lamba fuction

# a=lambda z:'positive' if z>0 else 'negative' if z>0 else 'zero'
# print(a(0))

# b=lambda a:'even' if a%2==0 else 'odd'
# print(b(12))

# two=lambda a,b:a*b
# print(two(3,4))

# s=lambda text:text.strip().lower()
# print(s('  TEJAS  '))

# employees = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# sorted_arr=sorted(employees,key=lambda x:x[1])
# print(sorted_arr)



# # The Doubler: Create a lambda function that takes one argument and returns it multiplied by 2.
# doubler=lambda x:x*2
# print(doubler(2))
# # The Last Letter: Create a lambda function that takes a string and returns only the last character of that string.
# lst_lt=lambda text:text[-1]
# print(lst_lt('Tejas'))
# # The Sales Tax: Create a lambda that takes a price and returns the price plus 18% tax (multiply by 1.18).
# tax=lambda x:x*1.18
# print(tax(300))

# # The Filter Prep (Harder): Create a lambda that takes a number and returns True if the number is greater than 100, otherwise False.
# k=lambda a:True if a>100 else False
# print(k(20))



# map fuctions in python

# def squre(a):
#     return a*a 
# n=[3,4,5,6,2]
# a=map(squre,n)
# print(list(a))


# num=[1,2,3,4,5,6]

# map1=map(lambda a:a*2,num)
# print(list(map1))


# cities = ["  mumbai            ", "pune  ", " DELHI ", "bangalore"]
# up1= list(map(lambda txt:txt.strip().lower(),cities))
# print(up1)
# 🚀 Mastery Practice: map() + lambdaTry these three tasks to lock in the concept:
# The Squarer: You have a list numbers = [2, 4, 6, 8]. Use map() and a lambda to create a new list where every number is squared ($x^2$).

# number=[2,4,6,8]
# s=list(map(lambda a:a*a,number))
# print(s)

# # The Initial Finder: You have a list of names players = ["Virat", "Dhoni", "Rohit"]. Use map() to create a list that only contains the first letter of each name.
# player=['Virat','Dhoni','Rohit']
# fst=list(map(lambda a:a[0],player))
# print(fst)

# The Price Converter: You have prices in Dollars usd_prices = [10, 20, 30]. Assuming 1 USD = 83 INR, use map() to create a list of these prices in INR.

# pri=[10,20,30]

# cvnt=list(map(lambda a: a*83,pri))
# print(cvnt)


# filter ...

# from functools import reduce


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Using lambda: logic is "x % 2 == 0"
# evens = list(filter(lambda x: x % 2 != 0, numbers))
# print(evens)
# # Output: [2, 4, 6, 8, 10]















# Problem 1: The "Product of Odds"
# Task:
# Take this list of numbers: numbers = [1, 2, 3, 4, 5, 6]
# Filter out the even numbers (keep only the odd ones: 1, 3, 5).
# Reduce the remaining numbers by multiplying them together to get a single product.
# Expected Output: 15 (because 1 * 3 * 5 = 15)

# from functools import reduce
# numbers = [1, 2, 3, 4, 5, 6]
# po=reduce(lambda x,y:x*y,filter(lambda x:x%2!=0,numbers))
# print(po)




# Problem 2: The "Clean Sentence" Builder
# Task:
# Take this messy list of strings: words = ["Python", "", "is", " ", "fun", "!", ""]
# Filter out any string that is empty or just contains whitespace (hint: use .strip()).
# Reduce the remaining words by joining them into a single sentence separated by spaces.
# Expected Output: "Python is fun !"
# from functools import reduce

# words = ["Python", "", "is", " ", "fun", "!", ""]
# cs=reduce(lambda txt,txt2:txt+" "+txt2,filter(lambda txt:txt.strip(),words))
# print(cs)


# Problem 3: The "VIP" Sum
# Task:

# Take this list of bank balances: balances = [5000, 200, 15000, 80, 50000]

# Filter to keep only "VIP" accounts (balances greater than 10,000).

# Reduce to find the total sum of money in these VIP accounts.

# Expected Output: 65000 (15000 + 50000)

# from functools import reduce
# balances = [5000, 200, 15000, 80, 50000]
# filterout=list(filter(lambda x:x>10000,balances))
# vipsum=reduce(lambda x,y:x+y,filterout)
# print(vipsum)



# Problem 4: The "Boss Level" (Map + Filter + Reduce)
# Since you know map as well, let's combine all three!
# Task:
# Take this list of prices: prices = [100, 250, 50, 400]
# Filter to keep only prices greater than 200.
# Map a 10% tax to those prices (multiply by 1.1).
# Reduce to find the total sum of these taxed prices.
# Expected Output: 715.0 (Logic: Keep 250 and 400. Tax them -> 275 and 440. Sum -> 715)

# from functools import reduce
# prices = [100, 250, 50, 400]

# imp=reduce(lambda x,y:x+y,map(lambda x:x*1.1,list(filter(lambda x:x>200,prices))))
# print(imp)


# from functools import reduce

# orders = [
#     {"id": 1, "status": "delivered", "price": 500, "qty": 2},
#     {"id": 2, "status": "canceled", "price": 1000, "qty": 1},
#     {"id": 3, "status": "delivered", "price": 50, "qty": 10},
#     {"id": 4, "status": "pending", "price": 200, "qty": 1},
#     {"id": 5, "status": "delivered", "price": 100, "qty": 5}
# ]


# a=list(filter(lambda x:x['status']=="delivered",orders))
# print("onley delivered status",a)

# b=list(map(lambda x:x['price']*x['qty'],a))
# print(b)

# c=reduce(lambda x,y:x+y,b)
# print(c)



# list comprehensions
# syntax is [ <ACTION> for <ITEM> in <LIST> if <CONDITION> ]

# a=[2,3,4,5,6,7]
# compre=[x*2 for x in a if x%2==0]
# print(compre)






# Snippet A: (Get lengths of words)

# Python

# words = ["apple", "banana", "kiwi"]
# lengths = list(map(lambda w: len(w), words))
# # Your task: Rewrite using [ ... ]


# new 
# getlen=[len(x) for x in words]
# print(getlen)







# Snippet B: (Get names that start with "A")

# Python

# names = ["Alice", "Bob", "Amanda", "Charlie"]
# a_names = list(filter(lambda n: n.startswith("A"), names))
# # Your task: Rewrite using [ ... ]

# getname=[x for x in names if x.startswith('A')]
# print(getname)



# Snippet C: (The Combo: Uppercase words longer than 4 letters)

# Python

# words = ["hi", "hello", "yo", "python"]
# big_words = list(map(lambda w: w.upper(), filter(lambda w: len(w) > 4, words)))
# # Your task: Rewrite using [ ... ]


# big_word=[x for x in words if len(x)>4]
# print(big_word)


orders = [
    {"id": 1, "status": "delivered", "price": 500, "qty": 2},
    {"id": 2, "status": "canceled", "price": 1000, "qty": 1},
    {"id": 3, "status": "delivered", "price": 50, "qty": 10},
    {"id": 4, "status": "pending", "price": 200, "qty": 1},
    {"id": 5, "status": "delivered", "price": 100, "qty": 5}
]
summ=[x['price']*x['qty'] for x in orders if x['status']=='delivered']
print(sum(summ))