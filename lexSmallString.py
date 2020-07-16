'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
Written By Austin Bursey
Created On: 6/12/2020
Updated On: 6/12/2020
'''
# def lexSort(string , subString, pivot,k):
#     temp = ""
#     chars = sorted(subString)
#     badChars = {}
#     for i in range(0,k ): 
#         if (chars[i] > pivot): 
#             badChars[i] = True
#         else:
#             temp+= chars[i]
#     temp += string[k:]
#     for i in badChars: 
#         temp += chars[i]
#     return temp 

def findMin(string): 
    n = len(string)
    min_ind = 0
    min_val = string[0]
    for i in range(0,n): 
        if (string[i] < min_val): 
            min_val = string[i]
            min_ind = i 
    return min_ind

def lexSort(string, k ) : 
    temp = ""

    while (len(string) > 0 ): 
        i = findMin(string[:k])
        temp += string[i]
        
        string = string[:i] + string[i+1:]

    return temp

if __name__ == "__main__": 
    string = "geeksforgeeks"
    k = 5

    result = lexSort(string,k)
    print(result)
