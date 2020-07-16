/*
C++ program,
Given a string and a pattern,
 find the starting indices of all occurrences of the pattern in the string.
  For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7]

[input file is 'SSO.txt']
[.exe is 'SSO.exe' ]
Written By Austin Bursey
Created On: 6/11/2020
Updated On: 6/11/2020
/6th real c++ program/ 
*/
#include <iostream>
#include <string.h>
#include <vector>
const int max_size = 2e4; 
using namespace std ; 
int main(){
    //get user input 
    string given_string; 
    string sub_string; 
    cin >> given_string; 
    cin >> sub_string;

    //initialize variables 
    int n = given_string.size();
    int m = sub_string.size();
    int i = 0 ,j  = 0;
    vector<int> locations; 
    //problem is actually possible
    if ( (i + m )< n ){
       
        while (i + m  < n ){

            string temp = given_string.substr(i ,  m ); 
            if (temp.compare(sub_string)  == 0 ){
                locations.push_back(i );
            }
            cout << temp << endl;

            i ++ ; 
        }
        
        if (locations.size() > 0 ){
            cout << "The occurences of substring [" << sub_string << "] within the string [" << given_string << "] are at indices: " << endl;
            cout << "[" << locations[0] ; 
            i = 1; 
            n = locations.size(); 
            while (i <n){
                cout << "," << locations[i]; 
                i++; 
            }
            cout << "]";
        }else {
            cout << "No occurences of substring [" << sub_string << "] exists within the string [" << given_string << "]." << endl;
        }
    }  else { //problem is not possible
        cout << "SubString is too large";
    }
   
    
}