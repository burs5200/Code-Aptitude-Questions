'''
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

Written By Austin Bursey
Created On: 7/16/2020
Updated On: 7/16/2020
'''
import numpy as np 
def sum_to_k(S,k): 
    
    n = len(S)
    dp_array = np.full((len(S)+1,k+1),False,dtype=bool)
    
    for i in range(len(S)+1) : 
        dp_array[i][0] = True
    for i in range(1,len(S)+1): 
        for j in range(1,k+1):
            val = S[i-1]
            if  j >= S[i-1] : 
                dp_array[i][j] = dp_array[i-1][j] or dp_array[i-1][j-S[i-1]]
            else : 
                dp_array[i][j] = dp_array[i-1][j]



        
            
    solution = np.zeros(0,dtype= int)
    find_the_answer(dp_array, n, k , solution, S)

def find_the_answer(dp_array, i , k , solution_set,S): 
    if (i == 0 and k == 0 ) : 
        print("{0}".format(solution_set))
        
        return 
    elif(i == 0 ) : 
        print("No Subsets")
        return  
    if (dp_array[i-1][k]) : 
        find_the_answer(dp_array, i-1 , k , solution_set,S)

    if(k >= S[i-1] and dp_array[i][k-S[i-1]]):
        solution_set = np.insert(solution_set,0,S[i-1])
        find_the_answer(dp_array,i-1, k-S[i-1] , solution_set, S )

if __name__ == "__main__":
    array = [1,2,3,4,5]
    k = 10
    
    sum_to_k(array, k )