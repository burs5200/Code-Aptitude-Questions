'''
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81]


Written By Austin Bursey
Created On: 7/26/2020
Updated On: 7/26/2020
'''
import numpy as np 
def square_order_sorted(array) :
    square_array = np.array(array)
    square_array = np.sort(square_array ** 2) 
    return square_array
    

def efficient_square_sorted(array): 
    temp = np.array(array) ** 2 
    n = len(temp) 


    square_array = [] 
    i = n -1 # for positive array biggest element is at the back after squaring  
    j = 0 # for negative array biggest element is at the front after squaring  
    while j <= i : 
        if temp[j] > temp[i] : 
            square_array.insert(0,temp[j])
            j +=1 
        else : 
            square_array.insert(0,temp[i])
            i -=1 
    return square_array



if __name__ == "__main__":
    array =[-9,-3,-2,-2,0]
    print("Original Array is : {0}\nSorted Square elements is : {1}".format(array, efficient_square_sorted(array)))