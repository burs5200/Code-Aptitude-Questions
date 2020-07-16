/*
C++ program to find intersection between two single linked lists. 
Written By Austin Bursey
Created On: 6/4/2020
Updated On: 6/4/2020
/first real c++ program/ 

*/

#include <iostream>
#include <cstdlib>
class Node{
    public : 
    int data;  
    Node* next; 
    Node(int new_value ){
        data = new_value; 
        next = nullptr; 
    }
}; 

int getCount(Node* head){
    int i = 0; 
    Node * current = head; 

    while(current != nullptr ){
        current = current -> next; 
        i ++; 
    }
    return i; 

}
void populate(Node* head, int start , int end ){ 
    for (int i = start; i < end ; i ++){
        Node * current  = new Node(i); 
        head -> next = current; 
        head = current; 
    }

}
Node * _Aux_findIntersect(Node* longer,Node * shorter,int diff ){
    // 'trim' values off longer that are too long to be an intersect
    for (int i = 0; i < diff ; i ++ ){
        longer = longer -> next; 
    };
    //checking both longer and shorter for prosterity sake, need only check one since now their length is the same 
    // could create a comparitor for the nodes but dont know how right now. 
    while (longer != nullptr && shorter != nullptr && longer != shorter){
        
        longer = longer -> next; 
        shorter = shorter -> next; 
    }
 
    //could again just check one 
    if (longer != nullptr && shorter != nullptr  && longer == shorter){
        return longer;
    }
    return nullptr; 
}
Node * findIntersect(Node * head1 , Node * head2, int diff ){
    //if diff >= 0 then first list is longer/equal to second
    Node * answer; 
    if (diff >= 0 ){
        answer = _Aux_findIntersect(head1,head2,abs(diff)); 
    }else{ //if diff < 0 then second list is longer than the first 
        answer = _Aux_findIntersect(head2,head1,abs(diff));
    }
    return answer; 

}


int main (){
    Node* head = new Node(1); 
    populate(head , 2, 10 );
    int val_to_intersect = 5; 
    Node * current = head ; 
    Node * head2 = new Node(11); 
    //add nodes to head 2 
    Node * tmp = new Node (5); 
    head2 ->next = tmp; 
    Node * tmp2 = new Node(99);
    tmp -> next = tmp2;  
    //get to tail of head 2; 
    Node * current2 = head2; 
    while (current2->next  != nullptr){
        current2 = current2->next; 
    }
    //get to intersect point 
    while (current != nullptr && current -> data != val_to_intersect  ){
        current = current -> next; 
    }
    //populating head 2 with an intersect 
    while (current != nullptr ){
        current2->next = current; 
        current = current -> next; 
        current2 = current2->next; 
        
    }
    
    int len_1 =   getCount(head) ;
    int len_2 =   getCount(head2) ;
    int diff = len_1 - len_2; 
    std::cout << "First Linked List count is : " <<  getCount(head) << "\n\n";
    std::cout << "Second Linked List count is : " <<  getCount(head2) << "\n";
    std::cout << "Difference between the first and the second is : " << diff << "\n"; 
    Node * answer = findIntersect(head,head2 , diff); 
    if (answer != nullptr){
        std::cout << "The intersection happens at node value : " << answer -> data << "\n";  
        std::cout << "The next value is : " << answer-> next  -> data ;  
    }else {
        std :: cout << "No intersection was found\n";
    }
}