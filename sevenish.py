if __name__ == "__main__": 
    n = int (input("What sevenish number are you looking for : "))
    i = 0
    power = 2**(i+1) -1
    while (power< n ): 
        i +=1 
        power = 2**(i+1) -1

    print(power)
    print(7**i)
    sevens = []
    for j in range(0, i, 1 ): 
        sevens.append(7**j)
    
    print(sevens)
    diff = power - (2**(i) -1) 
    print(diff)
    valsToAdd = n -diff 
    print(valsToAdd)
    stringVersion = "{0:b}".format(valsToAdd)
    print(stringVersion)
    total = 7**i 
    i = 0 
    for char in stringVersion: 
        if char == '1' : 
            total += sevens[i]


        i +=1     
    print("The %d sevenish number is %d"%(n , total))