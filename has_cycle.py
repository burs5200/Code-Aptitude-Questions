'''
Written By Austin Bursey
Created On: 6/2/2020
Updated On: 7/3/2020
'''
from Ugraph import Graph
from stack import Stack

def has_cycle(graph) : 
    '''
    Checks if the graph contains a cycle or not 

    Params: 
        graph - an undirected graph from Ugraph.py
    
    Returns: 
        True - if the graph contains a cycle 

        False - if the graph does not contain a cycle 

    '''
    dfs_stack = Stack()
    visited = {}
    parent = {}
    head = graph.edges[graph.vertices[0]]
    dfs_stack.add(head)
    visited[head.data] = None
    parent[head.data] = None
    # visited[head] = None 
    while (dfs_stack.peek() != None ) : 
        current = dfs_stack.pop()
        temp = graph.edges[current.data]

        while temp is not None : 
            if ( temp.data not in visited  ) :
                visited[temp.data] = None 

                parent[temp.data ] = current.data 
                dfs_stack.add(temp)
            elif parent[current.data] != temp.data  : 
                return True 
            temp = temp.next 
    return False 

if __name__ == "__main__" : 
    vertices = [0,1,2,3,4]
    graph = Graph(vertices)
    graph.add_edge(0, 1) 
    # graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    # graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    # graph.add_edge(3, 4)  
    print("The graph contains a cycle : {0}".format(has_cycle(graph)))