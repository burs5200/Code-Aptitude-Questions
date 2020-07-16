'''
The edit distance between two strings refers to the minimum number of character insertions, deletions,
 and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is
 three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Written By Austin Bursey
Created On: 6/23/2020
Updated On: 6/23/2020
'''


def findDistance(start, target) : 
    """
    Description : 

    Finds the minimum number of character insertions, deletions and substitutions required to change one strings to another,
    start and target and returns the minimum

    Parameters : 

    start - the string you would like to transform into the target string
    target - the target string you would like to arrive at from start string 

    Return: 
    stepNum - the number of character insertions , deletions and substitutions required to change from one string to another. 
    """
    n = len(start)
    m = len(target)
    #find number of deletions and insertions
    if (n > 0 ): 
        current = [0 for i in range(n+1)] #covers base condition where 
        previous = [i for i in range(n+1)] #covers base Scondition of target being empty 
    else : 
        return m
    for i in range(1,m+1): 
        for j in range(0,n+1 ): 
            letterFromTarget = target[:i+1]
            letterfromstart = start[:j+1]
            if j == 0 : 
                current[j] = i 
            elif target[i-1] != start[j-1]:
                current[j] = 1 + min(min(previous[j-1], previous[j]),current[j-1]) 
                
            else : 
                current[j] = previous[j-1]
        previous = current 
        current = [0 for i in range(n+1)] 
   
    return previous[n]





if __name__ == "__main__" : 
    String1 = "Kitten"
    String2 = "Sitting"
    print("The distance between %s and %s is : %d"%(String1, String2,   findDistance(String1, String2)))