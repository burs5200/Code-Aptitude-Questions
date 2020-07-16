/*
C++ program,
Given a string and a number of lines k, print the string in zigzag form.
In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line,
then back up to top right, and so on. 


[input file is 'zigzag.txt']
[.exe is 'zigzag.exe' ]
Written By Austin Bursey
Created On: 6/8/2020
Updated On: 6/11/2020
/5th real c++ program/ 
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
using namespace std; 
const int max_size = 300; 
int main(int argc , char ** argv){
    if (argc > 1 ){
        string file_name = argv[1]; 
        ifstream input_file; 
        input_file.open(file_name); 
        if (input_file){
            string data; 
            
            int depth; 

            //grab input 
            input_file >> data;
            input_file >> depth;
            
            //declare variables 
            const int length  = data.size();
            vector<string>output_lines;
            
            //fill vector 
            for (int i = 0; i < depth ; i ++){
                char temp [max_size]= ""; 
                memset(temp, ' ', length); 
                output_lines.push_back(temp); 
            }

            int i = 0 ; //depth
            int j = 0; //length
            bool upward = true;//motion of filling
            cout << "Hello";
            for (char c : data){
                cout << "i = "<<  i <<endl;
                cout << "j = "<<  j <<endl;
                cout << "c = " << c << endl;
                cout << endl<<endl << endl << "--------------------" << endl;
                output_lines[i][j] = c;
                
                if (upward){
                    i ++; 
                    if (i >= depth-1){
                        upward = false; 
                    
                    }
                }else {
                    i --; 
                    if (i <= 0 ){
                        upward = true;
                    }
                }

                j ++; 
            }

            for (string line : output_lines){
                cout << line << endl;
            }
            cout << data << endl; 
            cout << depth << endl; 
            cout << length << endl; 


        }
    }else {
        cout << "File must be provided upon execution\n"; 
    }
    
}