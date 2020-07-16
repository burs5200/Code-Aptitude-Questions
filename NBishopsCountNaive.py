'''
You are given N bishops, represented as (row, column) tuples on a M by M chessboard.
Write a function to count the number of pairs of bishops that attack each other.
 The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
Written By Austin Bursey
Created On: 6/23/2020
Updated On: 6/23/2020
'''
from scipy.special import comb
import time 
def attackingBishops(matrix): 
    '''
    Parameters
        - matrix  : 
                an M by M board with rows as strings in an array
                0 for empty spot 
                b for bishop 
                board :                 Generated with : 
                        [b 0 0 0 0]                     ["b 0 0 0 0","0 0 b 0 0","0 0 b 0 0","0 0 0 0 0","b 0 0 0 0"]
                        [0 0 b 0 0]
                        [0 0 b 0 0]
                        [0 0 0 0 0]
                        [b 0 0 0 0]   
    returns : 
        - Number of attacking bishops 

    '''
    board = [matrix[i].split() for i in range(len(matrix))]
    n = len(board)
    pishopPairs = 0 
    diagLines = []
    for i in range(n):
        
        for  j in range(n) : 
            if board[i][j] == 'b' : 
                diagLines.append((i,j )) 
    n = len(diagLines )
    for i in range(n):
        for j in range(i+1,n): 
            if (abs(diagLines[i][0] - diagLines[j][0]) == abs(diagLines[i][1] - diagLines[j][1])): 
                if (pishopPairs != 0 ): 
                    pishopPairs +=1
                else : 
                    pishopPairs = 1
    return pishopPairs

    
if __name__ == "__main__":
    start_time = time.time()
    matrix = ["b 0 0 0 0","0 0 b 0 0","0 0 b 0 0","0 0 0 b 0","b 0 0 0 0"]
    print("Number of pishop pairs is : %d"%(attackingBishops(matrix)))
    print("--- %s seconds ---" % (time.time() - start_time))