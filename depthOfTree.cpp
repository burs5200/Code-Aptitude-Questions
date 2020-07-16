/*
C++ program,
You are given a binary tree in a peculiar string representation. Each node is written in the form (lr), where l corresponds to the left child and r corresponds to the right child.
If either l or r is null, it will be represented as a zero. Otherwise, it will be represented by a new (lr) pair.
Here are a few examples:
•	A root node with no children: (00)
•	A root node with two children: ((00)(00))
•	An unbalanced tree with three consecutive left children: ((((00)0)0)0)
 
[input file is 'depth.txt']
[.exe is 'dot.exe' ]
Written By Austin Bursey
Created On: 6/8/2020
Updated On: 6/8/2020
/4th real c++ program/ 
*/
#include <iostream>
#include <fstream>

using namespace std;
int main(int argc , char** argv ){
    if (argc > 1 ){
        string file_name = argv[1]; 
        ifstream infile;
        infile.open(file_name);
        if (infile){

            string data; 
            infile >> data; 
            int i = 0 ; 
            int depth =0; 
            int max_depth = depth; 
            for (const char &c : data ){
                if (c == '('){
                    depth ++; 
                    if (depth > max_depth){
                        max_depth = depth;
                    }
                }else if (c == ')'){
                    depth --; 
                }
            }

            cout << "Tree is " << data << endl;
            cout << "Depth of Tree is " << max_depth << endl; 
            infile.close();
        }else {
            cout << "File does not exist"<< endl;
        }
        


        
    }else {
        cout << "File must be provided upon execution\n"; 
    }
     
}