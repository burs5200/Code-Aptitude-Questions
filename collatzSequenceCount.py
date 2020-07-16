'''
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
•	if n is even, the next number in the sequence is n / 2
•	if n is odd, the next number in the sequence is 3n + 1 
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
Written By Austin Bursey
Created On: 6/26/2020
Updated On: 6/28/2020
'''
import numpy as np 
import matplotlib.pyplot as plt
import time
from collatzSequence import collatz_steps
def addToArr(arr ,positive_int): 
    
    arr[positive_int-1]['Value'] = n 

#!TODO speed this up. It is wayy to slow for any kind of ordinary use. cant even do 100 000 
def createCSReport(n): 
    '''
    Description : 
        Find all steps for all positive integers <=n and graph the amount of steps
    
    Params: 
        n - the upper bound of the program to run sequences for 

    Returns: 
        None - graphs the plot
    '''
    dtype = [('Value', np.int32), ('Steps', np.int32),('Travelled',np.int8)]
    StructArr = np.zeros([1 ],dtype=dtype)#could be improved to dynamic at the cost of performance since numpy arrays arent meant to be expanded. 
  
    
    
   
    for i in range(n, -1 , -1 ) : 
        iEX = StructArr[np.where(StructArr['Value'] ==  i )]
       
        if iEX.size == 0    :
            
            positive_int = i 
            while positive_int != 1  : 


                exist = StructArr[np.where(StructArr['Value'] == positive_int)]
                existLen = exist.size

                #already found this value
                if existLen == 1  : 
                    #increment every value that lead to this value since the sequence from this to 0 never changes. 
                    StructArr['Steps'] = np.where(StructArr['Value']!= 0     , np.where(StructArr['Travelled'] == 0 , StructArr['Steps']+StructArr[np.where(StructArr['Value'] == positive_int)]['Steps'], StructArr['Steps'] ), StructArr['Steps'])  
                    positive_int = 1   
                
                else : 

                    
                    StructArr = np.append(StructArr,np.array([(positive_int,0,0)],dtype=dtype))

                    StructArr['Steps'] = np.where(StructArr['Value']!= 0 , np.where(StructArr['Travelled'] == 0 , StructArr['Steps']+1, StructArr['Steps'] ), StructArr['Steps'])
                

                    if positive_int % 2 == 0 : # even  
                        
                        positive_int //=2
                    else : 
                        positive_int = 3 * positive_int +1 



            StructArr['Travelled'] = np.where(StructArr['Value'] != 0, np.where(StructArr['Travelled'] == 0 , StructArr['Travelled']+1, StructArr['Travelled'] ) , StructArr['Travelled'])

    StructArr = np.sort(StructArr, 0) # sort by value
    StructArr = StructArr[:n] # cut of all values after n cause they werent part of the expirement
    #plt.plot(StructArr['Value'], StructArr['Steps'])
    #plt.show()
    return StructArr[np.where(StructArr['Steps'] == np.max(StructArr['Steps']))]['Value']
        
def findMaxStepCollatz(n): 
    '''
    Description : 
        Find the number that has the longest collatz sequence whose value is <= n 
    
    Params: 
        n - the upper bound of the program to run sequences for 

    Returns: 
        maxValue(int) - the value that has the longest sequence length. 
    '''
    maxValue = 1 # collatz sequence of 1 has length of 1  
    maxSteps = 1 
    for i in range(2, n ): 
        steps = collatz_steps(i) 
        if steps > maxSteps : 
            maxSteps = steps 
            maxValue = i 
    return maxValue
if __name__ == "__main__": 
    n = 1000000
    start_time = time.time()
    print("The max value with the longest sequence is %s"%(findMaxStepCollatz(n)))
    print("--- %s seconds ---" % (time.time() - start_time))