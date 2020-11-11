# Depth-first vs Breadth-first or DFS vs BFS
# BFS goes through all its neighbors then the neighbors neighbors
# DFS goes through the path till it can't anymore then the next neighbor


# Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

from collections import deque

class Graph:

    def __init__(self):
        # vertex_id --> set of neighbors
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def remove_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            print('Trying to remove non-existent vertex')
            return
        self.vertices.pop(vertex_id)
        print(f'after pop{self.vertices}')
        for remaining_vertex in self.vertices:
            self.vertices[remaining_vertex].discard(vertex_id)

    def remove_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self. vertices:
            print('Trying to remove non-existent vertex')
            return
        self.vertices[from_vertex_id].discard(to_vertex_id)

    # Adds a directed edge from from_vertex_id to to_vertex_id
    def add_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print('trying to add edge to non-existing node')
            return
        self.vertices[from_vertex_id].add(to_vertex_id)

    # Returns all outgoing edges from vertex_id
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

# Pseudocode => DFT Iterative

# procedure DFT_iterative(G, V) is
#     let S be a stack
#     S.push(v)
#     while S is not empty do
#         v = S.pop()
#         if v is not labeled as discovered then
#             label v as discovered
#             for all edges from v to w in G.adjacentEdges(v) do
#                 S.push(w)

    def dft(self, starting_vertex):
        visited = set()
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.vertices[currNode]:
                    stack.append(neighbor)

# Pseudocode => DFT Recursive

# procedure DFS(G, v) is
#     label v as discovered 
#     for all directed edges from v to w that are in G.adjacentEdges(v) do
#         if vertex w is not labeled as discovered then
#         recursively call DFS(G, w)

    def dfs(self, starting_vertex, goal_vertex):
        visited = set()
        stack = deque()
        # Push the current path your're on onto the stack, instead of just a single vertex
        stack.append([starting_vertex])
        while len(stack) > 0:
            currNode = stack.pop()
            currNode= currPath[-1] # the current node you're on is the last node in teh path
            if currNode == goal_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath) # make a copy of hte current path
                    newPath.append(neighbor)
                    stack.append(newPath)


# Pseudocode => BFT Search

# procedure BFT(G, root) is
#     let Q be a queue
#     label root as discovered
#     Q.enqueue(root)
#     while Q is not empty do
#         v:=q.enqueue()
#         if v is the goal then
#             return v
#         for all edges from v to w in G.adjacentEdges(v) do
#             if w is not labeled as discovered then
#                 label w as discovered
#                 w.parent := v
#                 Q.enqueue(w)


# Uses queue instead of stack like dft this is also not recursive
    def bft(self, starting_vertex):
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.vertices[currNode]:
                    queue.append(neighbor)


graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 1)

# graph.dft(1)
# Prints the following:
# 1
# 3
# 4
# 2

# graph.bft(1)
# Prints the following:
# 1
# 2
# 3
# 4




