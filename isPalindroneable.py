'''
Given a string, determine whether any permutation of it is a palindrome.
For example, carrace should return true, since it can be rearranged to form racecar,
 which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.

Written By Austin Bursey
Created On: 6/24/2020
Updated On: 6/24/2020
'''

def isPalindroneable(string): 
    '''
    Determines if the string entered has a permutation that is a palindrome

    returns 
        True if it is a palindrone
        False otherwise 
    '''

    charDict = {}
    for c in string : 
        if c in charDict : 
            charDict[c] +=1 
        else : 
            charDict[c] = 1 

    i = 0 
    n = len(charDict)
    odds = 0 
    for value in charDict.values(): 
        if value % 2 == 1 : 
            odds +=1 
        
        if (odds > 1 ): 
            return False
    return True    

if __name__ == "__main__":
    string = "carrapace"
    print(isPalindroneable(string))