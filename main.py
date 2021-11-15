import csv
from queue import Queue
import distutils

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
    
    def __init__(self, name, color, distance, pi) :
        self.name = name
        self.color = color
        self.d = distance
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
        adj_list[edge[0]].append(tuple(edge))

    print(adj_list)    
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


def get_adjacent_vertices(adj_list, vertex) :
    """

    Parameters:
        param adj_list: adjacency list
        type adj_list: dictionary
        
        param vertex: adjacent vertices found relative to this vertex
        type vertex: Vertex object

    Returns:
        adj_vertices: list of names of vertices adjacent to the vertex parameter

    """
    
    adj_vertices = []
    for edge in adj_list[vertex] :
        adj_vertices.append(edge[1])
    
    return adj_vertices

def breadth_first_search(adj_list, source_vertex) :
    """

    Parameters:
        param adj_list: adjacency list
        type adj_list: dictionary
        
        param vertex: vertex where search begins
        type vertex: Vertex object

    Returns: 
        None

    """
    
    Q = Queue()
    vertices = {}

    for vertex in adj_list.keys() :
        vertices[vertex] = Vertex(name = vertex, color = "White", d = float("inf"), pi = None)

    source_vertex.color = "White"
    source_vertex.d = 0
    source_vertex.pi = None

    Q.put(source_vertex)
    while Q.empty() is not True :
        u = Q.get()

        adj_vertices = get_adjacent_vertices(adj_list, u.name)
        for vertex in adj_vertices :
            v = vertices[vertex]
            if v.color == "White" :
                v.color = "Gray"
                v.d = u.d + 1
                v.pi = u.name
                Q.put(v)

        u.color = "Black"

    return None

''' Dijkstra's Algorithm Functions '''
def init(adj_list, src_vertex) :
    """    
    
    Parameters:
        param adj_list: adjacency list
        type adj_list: dictionary
        
        param src_vertex: starting vertex for Dijkstra's algorithm
        type src_vertex: Vertex object

    Returns:
        None

    """
    
    vertices = {}
    for vertex in adj_list :
        vertices[vertex] = Vertex(name = vertex, color = None, d = float("inf"), pi = None)
    src_vertex.d = 0
    
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

def dijkstras(adj_list, edge_weight, src_vertex) :
    """
    

    Parameters:
        param adj_list: adjacency list
        type adj_list: dictionary
        
        param edge_weight: weight of the edge between ______
        type edge_weight: number
        
        param src_vertex: the vertex where the algorithm starts
        type src_vertex: Vertex object

    Returns:
        None

    """
    init(adj_list, src_vertex)
    vertex_set = None
    
    return None

''' Main Function '''
def main() :

    # help(function_name): returns docstring for function function_name
    
    # read in vertices of graph
    vertices = read_csv_file("RomaniaVertices.txt")
    vertices = [x[0] for x in vertices]

    # Read in edges of graph
    edges = read_csv_file("RomaniaEdges.txt")
    #print(edges)
    
    # construct graph using Romania data
    romania_graph = build_adj_list(vertices, edges)
    #print_graph(romania_graph)


    return None

main()