'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Written By Austin Bursey
Created On: 6/12/2020
Updated On: 6/12/2020
'''


if __name__ == "__main__" : 
    array = [34, -50, 42, 14, -5, 86]
    current_max = 0
    highest_max = 0 
    array_size = len(array)
    for i in range(0,array_size): 
        highest_max += array[i] 
        if (highest_max < 0 ): 
            highest_max = 0 
        elif( highest_max > current_max) : 
            current_max = highest_max 
    print(current_max)