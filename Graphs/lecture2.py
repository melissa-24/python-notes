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

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
# print(graph)


graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 1)
print(graph)

# graph.remove_vertex(4)
# print(graph)
# Prints the following 
# {1: {2, 3}, 2: {4}, 3: {4}, 4: {1}}
# after pop{1: {2, 3}, 2: {4}, 3: {4}}
# {1: {2, 3}, 2: set(), 3: set()}


# graph.remove_vertex(3)
# graph.remove_vertex(2)
# graph.remove_vertex(1)
# print(graph)
# Prints the following
# {1: {2, 3}, 2: {4}, 3: {4}, 4: {1}}
# after pop{1: {2, 3}, 2: {4}, 3: {4}}
# after pop{1: {2, 3}, 2: set()}
# after pop{1: {2}}
# after pop{}
# {}

# graph.remove_edge(4, 1)
# print(graph)
# Prints the following {
# 1: {2, 3}, 2: {4}, 3: {4}, 4: {1}}
# {1: {2, 3}, 2: {4}, 3: {4}, 4: set()}


graph.remove_edge(5, 1)
print(graph)
# Prints the following
# {1: {2, 3}, 2: {4}, 3: {4}, 4: {1}}
# Trying to remove non-existent vertex
# {1: {2, 3}, 2: {4}, 3: {4}, 4: {1}}
