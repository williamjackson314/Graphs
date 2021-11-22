import csv
import queue as q
import heapq

''' Support Functions '''    
def read_csv_file(file_name) :
    """

    Parameters:
        param file_name: name of the file to read into list
        type file_name: csv file
        
    Returns: 
        data: list of the values from the csv file

    """
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    return data

class Vertex :
    
    def __init__(self, name, color, d, pi) :
        self.name = name
        self.color = color
        self.d = d
        self.pi = pi

''' Adjacency List Functions '''
def build_adj_list(vertices, edges) :
    """

    Parameters:
        param vertices: list of vertices for adjacency list
        type vertices: list
        
        param edges: list of edges for adjacency list
        type edges: list

    Returns:
        adj_list - dictionary of vertices and edges representing a graph

    """
    
    adj_list = {}

    for vertex in vertices :
        adj_list[vertex] = []

    for edge in edges :
        adj_list[edge[0]].append((edge[1], edge[2]))
        adj_list[edge[1]].append((edge[0], edge[2]))
  
    return adj_list

def print_graph(adj_list) :
    """

    Parameters:
        adj_list - adjacency list implemented as a dictionary

    Returns: 
        None

    """
    
    for vertex, edges in adj_list.items() :
        print(str(vertex) + " -> ", end='')
        for edge in edges :
            print(str(edge) + ", ", end='')
        print('\n')

def breadth_first_search(adj_list, source_vertex_name) :
    """

    Parameters:
        param adj_list: adjacency list
        type adj_list: dictionary
        
        param vertex_name: vertex where search begins
        type vertex_name: Vertex object

    Returns: 
        None

    """

    Q = []
    vertices = {}

    for vertex in adj_list.keys() :
        vertices[vertex] = Vertex(name = vertex, color = "White", d = float("inf"), pi = None)

    vertices[source_vertex_name].d = 0

    Q.append(vertices[source_vertex_name])
    while len(Q) > 0:
        u = Q.pop()

        for edge in adj_list[u.name]:

            # edge[0] = name of adjacent vertex
            # edge[1] = edge weight between vertices
            v = vertices[edge[0]]
            if v.color == "White" :
                v.color = "Gray"
                v.d = u.d + 1
                v.pi = u.name
                Q.append(v)

        u.color = "Black"

    return vertices

''' Dijkstra's Algorithm Functions '''
def print_path(vertex_list, src_vertex, dest_vertex):
    
    predecessor = vertex_list[dest_vertex.pi]
    print(dest_vertex.name + " <- ", end='')
    while (predecessor.name != src_vertex.name):
        print(predecessor.name + " <- ", end='')
        predecessor = vertex_list[predecessor.pi]
    print(src_vertex.name)
        
def init(adj_list, src_vertex_name) :
    """    
    
    Parameters:
        param adj_list: adjacency list
        type adj_list: dictionary
        
        param src_vertex: starting vertex for Dijkstra's algorithm
        type src_vertex: Vertex object

    Returns:
        vertices : a dictionary with vertex name as key and Vertex object as value

    """
    
    vertices = {}
    for vertex in adj_list :
        vertices[vertex] = Vertex(name = vertex, color = None, d = float("inf"), pi = None)
    vertices[src_vertex_name].d = 0
    
    return vertices
    
def relax(src_vertex, dest_vertex, edge_weight) :
    """
    
    Parameters:
        param src_vertex: the starting vertex
        type src_vertex:  Vertex object
        
        param dest_vertex: the ending vertex, _____
        type dest_vertex: Vertex object
        
        param edge_weight: the weight of the edge from src to dest
        type edge_weight: number

    Returns: 
        None

    """
    
    if dest_vertex.d > (src_vertex.d + edge_weight) :
        dest_vertex.d = src_vertex.d + edge_weight
        dest_vertex.pi = src_vertex.name

def dijkstras_algorithm(adj_list, src_vertex_name) :
    """

    Parameters:
        param adj_list: adjacency list
        type adj_list: dictionary
        
        param src_vertex_name: the vertex where the algorithm starts
        type src_vertex_name: Vertex object

    Returns:
        None

    """
    # initializes a dictionary of the form vertex_name : Vertex object
    vertices = init(adj_list, src_vertex_name)

    path_known = set(()) # set of vertices whose shortest path is known
    Q = [] # initialize priority queue
    for vertex in adj_list.keys() :
        vertex_tuple = (vertices[vertex].d, vertex) # build priority queue item
        heapq.heappush(Q, vertex_tuple) # add item to priority queue
    
    while len(Q) > 0 :
        u = heapq.heappop(Q)[1] # retrieve second value in priority queue tuple: vertex name
        path_known.add(u)
        
        #print(vertices[u].d)
        
        # edges in the adjacency list dictionary at key == u
        for edge in adj_list[u] :
            
            # edge[0] = name of adjacent vertex
            # edge[1] = edge weight between vertices
            if edge[0] not in path_known :
                
                relax(vertices[u], vertices[edge[0]], int(edge[1]))
                
                # Add tuple with adjusted d value to priority queue
                vertex_tuple = (vertices[edge[0]].d, edge[0])
                heapq.heappush(Q, vertex_tuple)

    return vertices

''' Main Function '''
def main() :

    # read in vertices of graph
    vertices = read_csv_file("RomaniaVertices.txt")
    vertices = [x[0] for x in vertices]

    # Read in edges of graph
    edges = read_csv_file("RomaniaEdges.txt")
    
    # construct graph using Romania data
    romania_graph = build_adj_list(vertices, edges)
    
    print("1: BFS\n2: Print Graph\n3: Dijkstras\n4: Quit")
    user_input = int(input())
    while user_input != 4 :
        if user_input == 1 :
            vertices = breadth_first_search(romania_graph, "Arad")
            print_path(vertices, vertices["Arad"], vertices["Sibiu"])
            print_path(vertices, vertices["Arad"], vertices["Craiova"])
            print_path(vertices, vertices["Arad"], vertices["Bucharest"])
        elif user_input == 2 :
            print_graph(romania_graph)
        elif user_input == 3 :
            vertices = dijkstras_algorithm(romania_graph, "Arad")
            print_path(vertices, vertices["Arad"], vertices["Bucharest"])
        else:
            print("Invalid choice, try again: ")
        
        print("1: BFS\n2: Print Graph\n3: Dijkstras\n4: Quit")
        user_input = int(input())

    
    return None

main()