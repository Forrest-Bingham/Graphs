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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        #Create set for visited vertices
        visited = set()

        while queue.size() > 0:
            #dequeue first vertex on queue
            current = queue.dequeue()
            #if has not been visited

            if current not in visited:
                print(current)

                #mark as visited
                visited.add(current)
                #add all unvisited neighbors to the queue
                for x in self.get_neighbors(current):
                    if x not in visited:
                        queue.enqueue(x)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        #Create set for visited vertices
        visited = set()

        while stack.size() > 0:
            #dequeue first vertex on queue
            current = stack.pop()
            #if has not been visited

            if current not in visited:
                print(current)

                #mark as visited
                visited.add(current)
                #add all unvisited neighbors to the queue
                for x in self.get_neighbors(current):
                    if x not in visited:
                        stack.push(x)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        #checks to see if visited is None
        if visited is None:
            #if it is none, change to set
            visited = set()

        #Add starting vertex to visited
        visited.add(starting_vertex)

        print(starting_vertex)
        #get neighbors from starting vertex
        neighbors = self.get_neighbors(starting_vertex)

        while len(neighbors) > 0:
            #loop through neighbors
            for x in neighbors:
                #if neighbor not in visited
                if x not in visited:
                    #run recursion again but with new vertex and visited
                    self.dft_recursive(x, visited)

                else:

                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        bft_path = Queue()

        bft_path.enqueue([starting_vertex])
        #create set for visited vertices
        visited = set()

        while bft_path.size() > 0:
            #dequeue first path
            current_path = bft_path.dequeue()
            #Grab last vertex in the path
            current_path_last = current_path[-1]
            #if it hasnt been visited

            if current_path_last not in visited:
                #check if target
                if current_path_last == destination_vertex:
                    #return if it is the target
                    return current_path
                #mark it as visited
                else:

                    visited.add(current_path_last)

                    neighbors = self.get_neighbors(current_path_last)

                    for x in neighbors:
                        #copy the path
                        copy = current_path[:]
                        #add the neighbor
                        copy.append(x)
                        #add new path
                        bft_path.enqueue(copy)


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
            
    def dfs_recursive(self, starting_vertex, destination_vertex, dfs_path=Stack(), visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()

        current_path = dfs_path.pop()

        if current_path is None:

            current_path = [starting_vertex]

        if current_path[-1] not in visited:

            visited.add(current_path[-1])

            for x in self.get_neighbors(current_path[-1]):

                if x == destination_vertex:

                    current_path.append(x)

                    return current_path

                copy = current_path.copy()

                copy.append(x)

                dfs_path.push(copy)

            return self.dfs_recursive(starting_vertex, destination_vertex, dfs_path, visited)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
