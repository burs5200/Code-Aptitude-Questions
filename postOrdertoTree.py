'''
Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.
For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:
    5
   / 
  3   7
 / \   
2   4   8


Written By Austin Bursey
Created On: 6/26/2020
Updated On: 6/26/2020
'''
class Node: 

    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def postOrderTreeGen(nodeArray): 
    '''
    Description: 
        Turns the post order array into a binary tree. 
    Parameters: 
        nodeArray - an array singifying the post order of a tree. the items in the array must be comparable

    Returns: 
        Root - the root of the tree passed in post order
    '''
    n = len(nodeArray)
    rootNum = nodeArray[n - 1 ]
    i = n -1 
    m = -1 
    while i > m  and nodeArray[i] > rootNum: 

        i -=1 
    
    
    
    

if __name__ == "__main__": 
    postOrderArray = [2, 4, 3, 8, 7, 5,]
    postOrderTreeGen(postOrderArray)