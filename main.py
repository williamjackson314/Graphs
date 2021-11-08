import csv

''' Support Functions '''    
def read_file(file_name) :

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    return data


def build_adj_list(vertices, edges) :
    
    adj_list = {}
    
    for vertex in vertices :
        adj_list[vertex[0]] = []
        
    for edge in edges :
        adj_list[edge[0]].append(tuple(edge))
        
    return adj_list

def print_graph(adj_list) :

    for vertex, edges in adj_list.items() :
        print(str(vertex) + " -> ", end='')
        for edge in edges :
            print(str(edge) + ", ", end='')
        print('\n')

def main() :

    # read in vertices of graph
    vertices = read_file("RomaniaVertices.txt")

    # Read in edges of graph
    edges = read_file("RomaniaEdges.txt")

    # construct graph using Romania data
    romania_graph = build_adj_list(vertices, edges)
    print_graph(romania_graph)


    return None

main()