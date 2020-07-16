
# Python3 program to find minimum  
# number of trials in worst case. 
  
# Find sum of binomial coefficients  
# xCi (where i varies from 1 to n).  
# If the sum becomes more than K 
def binomialCoeff(x, n, k): 
  
    sum = 0; 
    term = 1; 
    i = 1; 
    while(i <= n and sum < k):  
        term *= x - i + 1; 
        term /= i; 
        sum += term; 
        i += 1; 
    return sum; 
  
# Do binary search to find minimum  
# number of trials in worst case. 
def minTrials(n, k): 
  
    # Initialize low and high as  
    # 1st and last floors 
    low = 1; 
    high = k; 
  
    # Do binary search, for every  
    # mid, find sum of binomial  
    # coefficients and check if  
    # the sum is greater than k or not. 
    while (low < high): 
  
        mid = (low + high) / 2; 
        if (binomialCoeff(mid, n, k) < k): 
            low = mid + 1; 
        else: 
            high = mid; 
  
    return int(mid); 
  
# Driver Code 
print(minTrials(2, 10)); 
  
# This code is contributed  
# by mits 