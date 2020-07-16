'''
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
•	if n is even, the next number in the sequence is n / 2
•	if n is odd, the next number in the sequence is 3n + 1 
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.


Written By Austin Bursey
Created On: 6/26/2020
Updated On: 6/26/2020
'''
def is_collatz(positive_int): 
    '''
    Params: 
        positive_int - a positive integer that will be tested against the collatz sequence to see if the conjecture holds. 

    Returns: 
        True - if after m steps the next number in the sequence is 1. 

        false - if there are an infinite amount of steps without reaching 1. 
    '''
    #if not possible this will run an infinite loop. Kinda intentional. Add timer to  after 5 hours in future. 
    while positive_int != 1  : 
        if positive_int % 2 == 0 : # even  
            positive_int /=2
        else : 
            positive_int = 3 * positive_int +1 
    
    if positive_int == 1 : 
        return True 
    return False
    
def collatz_steps(positive_int): 
    '''
    Params: 
        positive_int - a positive integer that will be tested against the collatz sequence to see if the conjecture holds. 

    Returns: 
        steps (int) - the number of steps required for the sequence to reach 1 

    '''
        #if not possible this will run an infinite loop. Kinda intentional. Add timer to  after 5 hours in future. 
    i = 0 
    while positive_int != 1  : 
        if positive_int % 2 == 0 : # even  
            positive_int /=2
        else : 
            positive_int = 3 * positive_int +1 
        i += 1 

    return i
    
if __name__ == "__main__": 
    value = 1973
    print("Does the collatz sequence hold : %s"%("yes" if is_collatz(value) else "No"))