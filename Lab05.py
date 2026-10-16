################################## TASK 01##############################################
#########Write a program that will implement the following graph in python. ############
# Graph Class

# class Graph:
#     def __init__(self, v):
#         self.V = v
#         self.adj = [[] for i in range(v)]

#     def addEdge(self, v, w):
#         self.adj[v].append(w)

#     def traverse(self, s):
#         visited = [False] * self.V
#         queue = [s]

#         visited[s] = True

#         while len(queue) > 0:
#             current = queue.pop(0)
#             print(current, end=" ")

#             for i in self.adj[current]:
#                 if not visited[i]:
#                     visited[i] = True
#                     queue.append(i)


# # Driver Code
# g = Graph(5)

# g.addEdge(0, 1)
# g.addEdge(0, 4)
# g.addEdge(1, 0)
# g.addEdge(1, 4)
# g.addEdge(1, 3)
# g.addEdge(2, 1)
# g.addEdge(2, 3)
# g.addEdge(3, 1)
# g.addEdge(3, 2)
# g.addEdge(3, 4)
# g.addEdge(4, 0)
# g.addEdge(4, 1)
# g.addEdge(4, 3)
# print("Following is Breadth First Traversal")
# print("Starting from vertex 2:")
# g.traverse(2)

# ################################## TASK 02##############################################
# ######You are given the following tree whose starting node is A and Goal node is G .####
# # You are required to implement the following graph in python ###########################
# # and then apply the following search(Stop the search when goal is achieved) a) Breadth First Search using Queue.####
# from collections import deque

# class Graph:
#     def __init__(self, V):
#         self.V = V
#         self.adj = {}

#         for i in V:
#             self.adj[i] = []

#     def addEdge(self, v, w):
#         self.adj[v].append(w)

#     def BFS(self, start, goal):
#         visited = []
#         queue = [start]
#         visited.append(start)

#         while len(queue) > 0:
#             s = queue.pop(0)
#             print(s, end=" ")

#             if s == goal:
#                 print("\nGoal found!")
#                 return

#             for neighbor in self.adj[s]:
#                 if neighbor not in visited:
#                     visited.append(neighbor)
#                     queue.append(neighbor)

#         print("\nGoal not found!")


# g = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'])

# g.addEdge('A', 'B')
# g.addEdge('A', 'F')
# g.addEdge('A', 'D')
# g.addEdge('A', 'E')

# g.addEdge('B', 'K')
# g.addEdge('B', 'J')

# g.addEdge('D', 'G')

# g.addEdge('E', 'C')
# g.addEdge('E', 'H')
# g.addEdge('E', 'I')

# g.addEdge('K', 'N')
# g.addEdge('K', 'M')

# g.addEdge('I', 'L')

# g.BFS('A', 'Z')


# ################################## TASK 03##############################################
# #############################: Implement priority Queue. ###############################
class PriorityQueue:
    def __init__(self):
        self.pq = []

    def push(self, priority, item):
        self.pq.append((priority, item))

    def pop(self):
        self.pq.sort()
        return self.pq.pop(0)

    def display(self):
        while self.pq:
            priority, item = self.pop()
            print(item, "Priority:", priority)


pq = PriorityQueue()

pq.push(3, "C")
pq.push(1, "A")
pq.push(2, "B")

pq.display()