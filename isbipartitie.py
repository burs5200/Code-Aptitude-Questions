'''
Written By Austin Bursey
Created On: 6/30/2020
Updated On: 7/3/2020
'''
from Ugraph import Graph
from Queue import Queue

def is_bipartite(graph):
    '''
    Description : 
        - checks if an undirected graph is bipartite

    Params : 
        graph - an undirected graph made from Ugraph.py
    
    Returns : 
        True - if the graph has a bipartite split 

        False - if the graph does not contain a bipartite split 
    '''
    bfs_queue = Queue()
    head = graph.edges[graph.vertices[0]]#choose arbitraty starting vertex 
    bfs_queue.add(head) # start bfs 
    head.color = "Green"
    while(not bfs_queue.is_empty()): 
        node  = bfs_queue.remove()

        edge = graph.edges[node.data]
        while edge is not None : 
            if edge.color == None : #this vertex hasnt been visited yet so add it the to queue
                bfs_queue.add(edge)
            #if its time to color red and its not already in green , add it to red 
            if node.color == "Red" and edge.color != "Red":
                edge.color = "Green"  # yes this may cause some redundant assignments for even cycles 

            #if its time to color green and its not already in red , add it to green 
            elif node.color == "Green" and edge.color != "Green":
                edge.color = "Red" # yes this may cause some redundant assignments for even cycles 

            # if its already one color, and we go to paint it a different color, there is an odd cycle and thus is not bipartite
            else : 
                return False    
            edge = edge.next 


    return True


if __name__ == "__main__" :
    vertices = [0,1,2,3,4] 
    graph = Graph(vertices)
    graph.add_edge(0, 1) 

    graph.add_edge(1, 2) 
     
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4)  
    print("The graph is bipartite : {0}".format(is_bipartite(graph)))