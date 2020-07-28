'''
Written By Austin Bursey
Created On: 7/1/2020
Updated On: 7/3/2020
'''
import sys 
print(sys.version)
import numpy as np 
class GNode: 
    def __init__(self,data) : 
        self.data = data 
        self.next = None 
        self.color = None
class Graph : 

    def __init__(self, vertices) : 
        self.vertices = vertices
        self.edges = {}
        for vertex in vertices : 
            self.edges[vertex] = None 
    def get_first_adj_list(self):

        return self.edges[self.vertices[0]]

    def get_vertex_adj_list(self,i):
        return self.edges[i]
        
    def add_edge(self, start, dest ) : 
        endNode = GNode(dest) 
        strtNode = GNode(start)
        #add end node to start list 
        endNode.next = self.edges[start]
        self.edges[start] = endNode

        #add end node to start since undirected graph 
        strtNode.next = self.edges[dest]
        self.edges[dest] = strtNode
    
    def print_graph(self): 

        for vertex in self.edges.keys() : 
            print("Adjency List for {%s} is :"%(vertex))
            current = self.edges[vertex]
            while current is not None :
                print("{%s}->" %(current.data),end ="") 
                current = current.next 
            print("None")
    
    def to_adjency_matrix(self) : 
        '''
        INTEGER ONLY 
        '''
        n = len(self.vertices)
        matrix = np.zeros((n,n),dtype=int)# create an N by N matrix filled with zeroes
        
        for vertex in self.edges.keys(): 
            if not str(vertex).isdigit() :
                return False
            current = self.edges[vertex]
            while current is not None : 
                matrix[vertex][current.data] = 1 
                current = current.next 
        return matrix 
        

if __name__ == "__main__" :
    vertices = [0,1,2,3,4] 
    temp = Graph(vertices)
    temp.add_edge(0, 1) 
    temp.add_edge(0, 4) 
    temp.add_edge(1, 2) 
    temp.add_edge(1, 3) 
    temp.add_edge(1, 4) 
    temp.add_edge(2, 3) 
    temp.add_edge(3, 4) 
    temp.print_graph()
    matrix = temp.to_adjency_matrix()
    n = len(matrix )
    print("   ",end="")
    for i in range (n) : 
        print("{0:^3} ".format(i),end = "")
    print()
    for i in range(n) :
        print("{0:^3}".format(i),end ='')
        for j in range(n) : 
            print("[{matrix}]".format(matrix= matrix[i][j]), end = " ")
        print()