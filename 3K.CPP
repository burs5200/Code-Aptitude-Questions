/*
C++ program to find intersection between two single linked lists. 
Written By Austin Bursey
Created On: 6/5/2020
Updated On: 6/5/2020
/Second real c++ program/ 

*/
#include <iostream>
#include <cstdlib>
#include <array> 
#include <algorithm>
int main(){
    //Input
    std::array<int,10> nums = {1,42,3,6,7,58,2,15,75,100 }; 
    int k = 73; 

    //sort the vector here 
    sort (nums.begin(), nums.end());
    //defined for the question 
    int n = nums.size();
    bool answer = false; 
    int i = 0; 
    int start; 
    int end; 

    //begin loop
    while(i < n && ! answer ){//O(N^2)
        start = 0 ; 
        end = n -1; 

        //reduce problem to finding two numbers in an array to match a new k 
        int pair_k = k - nums[i];

        
        while (start < end  && !answer){ // O(N) 

            //checks to 'skip' start or end  == i could be improved upon. 
            if (start != i ){
                if (end != i ){

                    //move indices down or up based on sum compared to k 
                    int test = nums[start] + nums[end]; 
                    if (test == pair_k){
                        
                        answer  = true; 

                    }else if(test > pair_k){
                        end --; 
                    }else {
                        start ++; 
                    }



                }else {
                    end --; 
                }
            }else{
                start ++; 
            }

        }
        if (!answer ){// purely for output purposes to keep i the same after last iteration. 
            i ++ ; 
        }
        
    }
    if (answer ){
        std::cout << "K was found using indices i : " << i <<  ", start: " << start << ", end: " << end << "\n"  ;
        std::cout << "Values are : " << nums[i] << ", "<<nums[start] << "," <<nums[end] <<" Respectively.\n";  
    }else{
        std::cout << "K was not found";
    }

}