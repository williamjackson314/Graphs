# Required Modules
* csv : used to read in csv files
* heapq : used to implement min priority queue for Dijkstra's Algorithm

# Data Formatting
- Vertices :
    * Data shall be in csv format, with only one column containing the name of each vertex
- Edges :
    * Data shall be in csv format, with three columns, representing undirected edges:
        starting node, descendent node, edge weight

# Graphs

**Data Structures**

Adjacency List:
    Dictionary:
        * Key: vertex name
        * Value: 
            - list of tuples where each tuple is an edge of the graph connected to the vertex specified
              by the key. Tuples have two parts: (adjacent vertex name, edge weight)

Class Vertex:
    Has four fields:
        * name: name of vertex
        * color: either 'White', 'Gray', or 'Black'. Used ofr BFS
        * d: the smallest total pth weight to get from a specified src vertex to this vertex
        * pi: the name of the previously visited vertex that is connected to this vertex 


**1. Breadth First Search**
* Queue: the BFS implementation needs a queue. This was implemented using a list and the append() and pop() methods. 
* Print Path: the path printout from Arad to Bucharest is given in the main code, this is:
    
    Bucharest <- Pitesti <- RimnicuVilcea <- Sibiu <- Arad
    
    
**2. Print Graph**
For the "Romania Graph implementation provided, the printout is shown below:

        Arad -> ('Zerind', '75'), ('Timisoara', '118'), ('Sibiu', '140'), 
        
        Bucharest -> ('Urziceni', '85'), ('Giurgiu', '90'), ('Pitesti', '101'), ('Fagaras', '211'), 
        
        Craiova -> ('Dobreta', '120'), ('Pitesti', '138'), ('RimnicuVilcea', '146'), 
        
        Dobreta -> ('Craiova', '120'), ('Mehadia', '75'), 
        
        Eforie -> ('Hirsova', '86'), 
        
        Fagaras -> ('Bucharest', '211'), ('Sibiu', '99'), 
        
        Giurgiu -> ('Bucharest', '90'), 
        
        Hirsova -> ('Eforie', '86'), ('Urziceni', '98'), 
        
        Iasi -> ('Neamt', '87'), ('Vaslui', '92'), 
        
        Lugoj -> ('Mehadia', '70'), ('Timisoara', '111'), 
        
        Mehadia -> ('Dobreta', '75'), ('Lugoj', '70'), 
        
        Neamt -> ('Iasi', '87'), 
        
        Oradea -> ('Zerind', '71'), ('Sibiu', '151'), 
        
        Pitesti -> ('Bucharest', '101'), ('Craiova', '138'), ('RimnicuVilcea', '97'), 
        
        RimnicuVilcea -> ('Craiova', '146'), ('Pitesti', '97'), ('Sibiu', '80'), 
        
        Sibiu -> ('Arad', '140'), ('Fagaras', '99'), ('Oradea', '151'), ('RimnicuVilcea', '80'), 
        
        Timisoara -> ('Arad', '118'), ('Lugoj', '111'), 
        
        Urziceni -> ('Bucharest', '85'), ('Hirsova', '98'), ('Vaslui', '142'), 
        
        Vaslui -> ('Iasi', '92'), ('Urziceni', '142'), 
        
        Zerind -> ('Arad', '75'), ('Oradea', '71'), 


**3. Dijkstra's Algorithm**
* Min Priority Queue: used heapq to implement, especially the push() and pop() methods.
* Set: used the set() and add() methods to implement the shortest known path set.
* Print Path: the path printout from Arad to Bucharest is given in the main code, this is the same as that
              found using the BFS algorithm:
    
        Bucharest <- Pitesti <- RimnicuVilcea <- Sibiu <- Arad


