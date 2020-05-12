"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        
        else:
            raise IndexError(f'The vertex does not exist at {v1} and {v2}')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

     def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        dfs_path = Stack()

        dfs_path.push([starting_vertex])
        
        visited = set()

        while dfs_path.size () > 0:

            current_path = dfs_path.pop()

            current_path_last = current_path[-1]

            if current_path_last not in visited:

                if current_path_last == destination_vertex:

                    return current_path

                
                else:

                    visited.add(current_path_last)
                    neighbors = self.get_neighbors(current_path_last)

                    for x in neighbors:

                        copy = current_path[:]

                        copy.append(x)

                        dfs_path.push(copy)


    def earliest_ancestor(ancestors, starting_node):
    #test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    #Create a graph
    ancestor_graph = Graph()

    #Create a path
    path = []
    
    #add vertices

    #add edges

    #Add paths 