'''
Given an undirected graph, check if the graph is minimally-connected.
 You can choose to represent the graph as either an adjacency matrix or adjacency list
Written By Austin Bursey
Created On: 7/26/2020
Updated On: 7/26/2020
'''
from Ugraph import Graph
from stack import Stack 
def is_min_connected(graph) : 
    dfs_stack = Stack()
    adj_list = graph.get_first_adj_list()
    while (adj_list is not None ) : 
        dfs_stack.add(adj_list)
        adj_list = adj_list.next
    
    visited = {}
    back_edges = False 
    
    while dfs_stack.peek() is not None and not back_edges: 
        node = dfs_stack.pop()
        if node.data in visited: 
            back_edges = True 
        else : 
            visited[node.data] = True 
            node_adj_list = graph.get_vertex_adj_list(node.data)
            while node_adj_list is not None : 
                dfs_stack.add(node_adj_list)
                node_adj_list = node_adj_list.next

    print(adj_list)
if __name__ == "__main__":
    vertices = [0,1,2,3,4]
    temp = Graph(vertices)
    temp.add_edge(0, 1) 
    temp.add_edge(0, 3) 
    temp.add_edge(1, 2)  
    temp.add_edge(3, 4)
    is_min_connected(temp)