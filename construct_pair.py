'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair)
 returns the first and last element of that pair.
  For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Written By Austin Bursey
Created On: 7/26/2020
Updated On: 7/26/2020
'''

def cons(a, b):
    
    def pair(f):
        return f(a, b)
    return pair # returns a function 'pair' that takes as input:  a function 'f' 



def car(pair) :  
    def f (a,b): #creates a function 'f' to use as input for the 'pair' function
        return a 
    
    return  pair(f) 

def cdr(pair): 
    def f(a,b):#creates a function 'f' to use as input for the 'pair' function
        return b 
    return pair(f)

if __name__ == "__main__":
    pair = cons(3,4)
    print(car(pair))
    print(cdr(pair))