'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
Written By Austin Bursey
Created On: 6/12/2020
Updated On: 6/12/2020
'''

def clockwisePrint(matrix , n, m):
    print("m = %d n = %d" %(m,n))
  
    row = 0 
    col = 0 
    while (col < m  and row < n ): 
        #going left 
        for i in range(col, m ) : 
            print(matrix[col][i])
        
        row +=1 

        #going down
        for j in range(row , n ): 
            print(matrix[j][m-1])
        m -=1

        #go right
        if (col < m ): 
            for i in range(m, col , -1 ): 
                print(matrix[n-1][i-1])

            n-=1
        #go up
        if (row  < n ) : 
            for j in range(n  , row , -1 ):
                print(matrix[j-1][col])

            col +=1 


def counterClockwisePrint(matrix, n, m ) : 
    row = 0 
    col = 0 
    print("Counter clock")

    while (col < m and row < n ): 
        #go down
        for i in range (row,n ): 
            print(matrix[i][row])
        col +=1 
        #go right 
        for i in  range(col, m ): 
            print(matrix[n -1 ][i ])
        n -= 1 
        #go up 
        if (row < n ) : 
            for i in range(n , row , -1 ): 
                print(matrix[i-1][m-1 ])
            m -=1 
        
        #go left 
        if (col < m ): 
            for i in range (m ,col , -1 ): 
                print(matrix[row][i-1])
            row +=1;
if __name__ == "__main__" : 
    matrix = [[1,  2,  3,  4,  5],[6,  7,  8,  9,  10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20]]
    clockwisePrint(matrix, len(matrix), len(matrix[0]))
    print("-"*18)
    counterClockwisePrint(matrix, len(matrix), len(matrix[0]))