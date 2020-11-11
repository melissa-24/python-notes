class Graph:

    def __init__(self):
        # vertex_id --> set of neighbors
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    # Adds a directed edge from from_vertex_id to to_vertex_id
    def add_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print('trying to add edge to non-existing node')
            return
        self.vertices[from_vertex_id].add(to_vertex_id)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
# print(graph)
# Prints the following 
# {1: set(), 2: set(), 3: set(), 4: set()}

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 1)
# print(graph)
# Prints the following 
# {1: {2, 3}, 2: {4}, 3: {4}, 4: {1}}

print(graph.get_neighbors(1)) #2, 3
print(graph.get_neighbors(4)) # 1
# Prints the following 
# {2, 3}
# {1}