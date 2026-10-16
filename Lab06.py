# ########################TASK 01#################################
# #  Graph class represents a directed graph
# # using adjacency list representation


# class Graph:

#     def __init__(self, V):
#         self.V = V
#         self.adj = [[] for _ in range(V)]

#     # Add an edge to the graph
#     def addEdge(self, v, w):
#         self.adj[v].append(w)

#     # Recursive DFS helper function
#     def DFSUtil(self, v, visited):
#         visited[v] = True
#         print(v, end=" ")

#         for i in self.adj[v]:
#             if not visited[i]:
#                 self.DFSUtil(i, visited)

#     # Recursive DFS
#     def DFSRecursive(self, v):
#         visited = [False] * self.V

#         print("Recursive DFS:")
#         self.DFSUtil(v, visited)
#         print()

#     # Iterative DFS using Stack
#     def DFSIterative(self, v):
#         visited = [False] * self.V
#         stack = [v]

#         print("Iterative DFS:")

#         while stack:
#             node = stack.pop()

#             if not visited[node]:
#                 visited[node] = True
#                 print(node, end=" ")

#                 # Reverse the order to match recursive DFS
#                 for i in reversed(self.adj[node]):
#                     if not visited[i]:
#                         stack.append(i)

#         print()


# # Create graph according to Task 1 diagram
# g = Graph(13)

# g.addEdge(1, 2)
# g.addEdge(1, 7)
# g.addEdge(1, 8)

# g.addEdge(2, 3)
# g.addEdge(2, 6)

# g.addEdge(3, 4)
# g.addEdge(3, 5)

# g.addEdge(8, 9)
# g.addEdge(8, 12)

# g.addEdge(9, 10)
# g.addEdge(9, 11)


# # Run both DFS methods
# g.DFSRecursive(1)
# g.DFSIterative(1)

#########################TASK 02###################################



class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {v: [] for v in vertices}

    # Function to add an edge to graph
    def addEdge(self, v, w):
        self.adj[v].append(w)

    # DFS using Stack
    def DFS(self, start, goal):

        visited = set()
        stack = [start]
        found = False

        while stack:

            v = stack.pop()

            if v not in visited:

                visited.add(v)

                # Print visited vertex
                print(v, end=" ")

                # Check if goal is found
                if v == goal:
                    print("\nGOAL FOUND!")
                    found = True
                    break

                # Push adjacent nodes in reverse order
                for i in reversed(self.adj[v]):

                    if i not in visited:
                        stack.append(i)

        # If goal was not found
        if not found:
            print("\nGOAL NOT FOUND!")


# Vertices of the graph
vertices = [
    'A', 'B', 'F', 'D', 'E',
    'K', 'J', 'G', 'C', 'H', 'I',
    'N', 'M', 'L'
]

# Create graph
g = Graph(vertices)

# Add edges
g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('A', 'D')
g.addEdge('A', 'E')

g.addEdge('B', 'K')
g.addEdge('B', 'J')

g.addEdge('K', 'N')
g.addEdge('K', 'M')

g.addEdge('D', 'G')

g.addEdge('E', 'C')
g.addEdge('E', 'H')
g.addEdge('E', 'I')

g.addEdge('I', 'L')


# Perform DFS using Stack
print("Depth First Search using Stack")
print("Starting from A and searching for Z:")

g.DFS('A', 'Z')

