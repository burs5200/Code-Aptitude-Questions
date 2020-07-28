'''
Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
Written By Austin Bursey
Created On: 7/28/2020
Updated On: 7/28/2020
'''

def min_max(array): 
    n = len(array)
    
    if n % 2 == 0 : 
        min_val = array[0]
        max_val = array[1]
    else : 
        min_val = array[0]
        max_val = array[0]

    i = 0 
    comparisons = 0 
    while i +1 < n : 
        temp_i = array[i]
        temp_j = array[i+1 ]
        if temp_i < temp_j : 
            if temp_i < min_val : 
                min_val = temp_i
            if temp_j > max_val : 
                max_val = temp_j
        else: 
            if temp_j < min_val : 
                min_val = temp_j
            if temp_i > max_val : 
                max_val = temp_i 
        i+=2 
        comparisons +=3 
    print("number of allowed comparisons : {0}\nNumber of comparisons used:{1}".format(2*(n-2),comparisons ))

if __name__ == "__main__":
    array = [-9,0,1,2,3,4,5,-20,99,12,300,-99 ]
    min_max(array)