/*
C++ program, with three variables x, y and b, if b is 1 return x if b is 0  return  y . 
Written By Austin Bursey
Created On: 6/6/2020
Updated On: 6/6/2020
/Third real c++ program/ 

*/
#include <iostream>
int decider(int x , int y , int b ){
    b = -b;
    return (x & b ) | (y & ~b);
}

int main(){
    int b = 0; 
    int x = 15; 
    int y = 25; 
    std::cout << decider(x,y,b); 


}