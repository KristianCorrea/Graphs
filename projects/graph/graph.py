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
            print("Error adding edge: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in
        beginning from starting_vertex.
        """
        # create an empty queue and 
        q = Queue()
        # enqueue A PATH TO the starting vertex ID
        q.enqueue(starting_vertex)

        visited = set() #Create a set for traversed vertices.  Create a Set to store visited vertices

        # while the queue is not empty...
        while q.size() > 0:
            # dequeue vertice 
            v = q.dequeue()
            # while queue is not empty
            print(v)
            if v not in visited:
            
                # mark as visited
                visited.add(v)
                # add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
            print(q.queue)
        
        print(visited)


    # DFS looks at each adjacent node,
    # and looks at all the children of the current adjacent nodes. 
    # It again, looks at the children of the next adjacent node.
    def dft(self, starting_vertex): 
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack
        s = Stack()
        # add starting vertex to stack
        s.push(starting_vertex)
        # create set for visited vertexes
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop a vert
            v = s.pop()
            # if not visited
            if v not in visited:
                # visit it
                print(v)
                # mark as visited
                visited.add(v)
                # add all neighbors to the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # added visited to parameter set default to None
        # DON'T set default to set()
        # first time around creates visited set()
        # keeps track of visited
        if visited == None:
            # creates visited set if None
            visited = set()
        # add to visit
        visited.add(starting_vertex)
        print("DFT Recursive Current Vertex: ", starting_vertex)
        # loop through
        for edge in self.vertices[starting_vertex]:
            # check if not in visited recursive function
            if edge not in visited:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and 
        q = Queue()
        # enqueue A PATH TO the starting vertex ID
        q.enqueue([starting_vertex])
        # create a Set to store visited vertices
        visited = set()
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first PATH
            path = q.dequeue()
            # grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited..
            if v not in visited:
                # CHECK IF ITS THE TARGET
                    #IF SO, RETURN PATH
                if v == destination_vertex:
                    return path
                # mark it as visited ...
                visited.add(v)
                #then add A PATH TO its neighbors to the back of the queue
                    # COPY THE PATH
                    # APPEND THE NEIGHBOR TO THE BACK
                for next_vert in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack
        s = Stack()
        # add starting vertex to stack
        s.push([starting_vertex])
        # create set for visited vertexes 
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop a vert
            path = s.pop()
            # if not visited
            if path[-1] not in visited:
                # if it is target, return
                if path[-1] == destination_vertex:
                    return path
                # if Not add to visit
                visited.add(path[-1])
                # add
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # added visited and path to paramenter
        # then set default to None
        # first time around creates set and list
        # creates visited set if None
        if visited == None:
            visited = set()
        # creates path [] if None
        if path == None:
            path = []
        # adds to visited
        visited.add(starting_vertex)
        # makes a copy of the path
        path = path + [starting_vertex]
        # check if it has reached its destination
        if starting_vertex == destination_vertex:
            return path
        # go through all neighbors
        for neighbor in self.vertices[starting_vertex]:
            # if not visited
            if neighbor not in visited:
                # neighbor becomes starting vert, recursive call
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # returns if there is a neighbor_path
                if neighbor_path is not None:
                    return neighbor_path
        # return None if neighbor_path is None
        return None

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
    print("BFT", graph.bft(1))

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
    print("BFS", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS", graph.dfs(1, 6))
    print("DFS Recursive", graph.dfs_recursive(1, 6))
