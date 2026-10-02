# ######################Task 1 without class##################### 
# stack = []

# # Push
# stack.append(100)
# stack.append(200)
# stack.append(300)

# print("Stack:", stack)

# # Pop
# item = stack.pop()
# print("Removed:", item)

# print("Stack after pop:", stack)

############### TASK 02 without class ###################

# queue = []

# # Enqueue
# queue.append(100)
# queue.append(200)
# queue.append(300)

# print("Queue:", queue)

# # Dequeue
# item = queue.pop(0)
# print("Removed:", item)

# print("Queue after dequeue:", queue)

##############Task 3##################

# numbers = [10, 20, 30, 40, 50]

# target = 40

# low = 0
# high = len(numbers) - 1

# while low <= high:

#     mid = (low + high) // 2

#     if numbers[mid] == target:
#         print("Found at index:", mid)
#         break

#     elif numbers[mid] < target:
#         low = mid + 1

#     else:
#         high = mid - 1

################Task 1 with class###################
# class Stack:

#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         return self.stack.pop()

#     def display(self):
#         print(self.stack)


# s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)

# s.display()

# s.pop()

# s.display()

############Task 2 with class############33

# class Queue:

#     def __init__(self):
#         self.queue = []

#     def enqueue(self, item):
#         self.queue.append(item)

#     def dequeue(self):
#         return self.queue.pop(0)

#     def display(self):
#         print(self.queue)


# q = Queue()

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)

# q.display()

# q.dequeue()

# q.display()


######### reverse string  ##########
s = input("Enter a string: ")

stack = []

# Pushing characters into stack
for ch in s:
    stack.append(ch)

# Poping characters to reverse and store it in reverse
reverse = ""
while stack:
    reverse += stack.pop()

print("Reversed string:", reverse)