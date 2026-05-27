# # class ab:
# #     def __init__(self,a,b):
# #         self.b=a
# #         self.a=b
    
# #     def sumofthis(self):
# #         summ=self.b+self.a
# #         return summ
    
# # a=ab(2,3)
# # print(a.sumofthis())


# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.next = node3

# # We call the first node the 'head' of the list
# head = node1

# # 1. Start our 'current' pointer at the head
# current = head

# # 2. YOUR TURN: Write the while loop!
# # It should run as long as 'current' is not None.
# # Inside the loop: print current.val, then move current to current.next

# while current != None:
#     print(current.val,end="-->")
#     current = current.next



# # --------------------------------------------------------


# # class Node:
# #     def __init__(self, value):
# #         self.val = value
# #         self.next = None

# # # 1. Create the nodes
# # node1 = Node(10)
# # node2 = Node(20)
# # node3 = Node(30)

# # # 2. Link them together!
# # # YOUR TURN: Make node1 point to node2
# # node1.next =node2

# # # YOUR TURN: Make node2 point to node3
# # node2.next = node3

# # # Let's test if it worked:
# # print("Node 1's value:", node1.val)
# # print("Node 2's value (accessed through Node 1):", node1.next.val)


# stack implemnetation

# stack=[]

# stack.append(10)
# stack.append(20)
# stack.append(30)

# print(stack)

# pop operation

# stack=[10, 20, 30]

# stack.pop()
# print(stack)






# stack implementation 

# class Stack:
#     def __init__(self):
#         self.stack=[]
    
#     def push(self,a):
#         return self.stack.append(a)
    
#     def pop(self):
#         return self.stack.pop()
    
#     def peek(self):
#         return self.stack[-1]
    
#     def display(self):
#         return self.stack

# s=Stack()

# s.push(12)
# s.push(14)
# s.push(15)

# print(s.display())


# print("Pop:", s.pop())

# print("Top:", s.peek())



# queue implementations in 

# class Queue:

#     def __init__(self):
#         self.queue=[]
    
#     def enqueue(self,item):
#         self.queue.append(item)
#         print(item,"added to queue")
    
#     def dequeue(self):
#         if len(self.queue)==0:
#             return "Queue is empty"
#         return self.queue.pop(0)
    
#     def display(self):
#         print(self.queue)

# q=Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)

# q.display()

# print("removal",q.dequeue())

# q.display()



# from collections import deque
# stack = deque()

# stack.append('a')
# stack.append('b')
# stack.append('c')

# print('initial stack:')
# print(stack)


# print('\n element popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print('\n stack after element are popped:')
# print(stack)



# def fib(c):
#     a,b=0,1
#     for i in range(c):
#         print(a,end=" ")
#         a,b=b,a+b
# fib(10)

# a=['asdf',10,'e',12]

# for i,v in enumerate(a):
#     print(i,v)


# def fibonacci(n):
#     a,b=0,1
#     for i in range(n):
#         yield b
#         a,b=b,a+b

# print(list(fibonacci(5)))
# counting value occurance............................
# a=[2,2,3,4,5,1,2,3,4]
# count={}

# for i in a:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1

# for i,v in count.items():
#     if v>2:
#         print(i)

# print(count)