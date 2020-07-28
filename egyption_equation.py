'''
The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one.
 For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468

Written By Austin Bursey
Created On: 6/26/2020
Updated On: 6/26/2020
'''
from math import ceil
def fraction_to_egyptian(denum , numer ) : 
    arr_of_denums = [] 
    arg1= denum
    arg0 = numer
    while numer != 0 : 
        new_denum = ceil(denum / numer)
        arr_of_denums.append(new_denum)
        
        numer  = (numer * new_denum) - denum
        denum *= new_denum 
        
    print("{0}/{1} can be represented as : ".format(arg0, arg1))
    print("1/{0}".format(arr_of_denums[0]),end="")
    for denum in arr_of_denums[1:] : 
        print(" + ",end="")
        print("1/{0}".format(denum), end="") 

if __name__ == "__main__":
    denum = 13 
    numer = 4 
    fraction_to_egyptian(denum,numer)