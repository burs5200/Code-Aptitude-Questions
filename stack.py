class Node : 
    def __init__(self,value) :
        self.value = value
        self.next = None
    
class Stack : 
    def __init__(self) : 
        self.head = None 
    
    def add(self,value) : 
        newHead = Node(value )
        newHead.next = self.head 
        self.head = newHead 
    
    def pop(self) : 
        if self.head is not None : 
            removedNode = self.head 
            self.head = self.head.next 
            return removedNode.value
        
        return None

    def peek(self ) : 
        if self.head is not None : 
            return self.head.value
        return None 

if __name__ == "__main__":
    stack = Stack()
    for i in range(5) : 
        stack.add(i)
    
    print("Top of stack is :{0}".format(stack.peek()))
    for i in range(3) : 
        print("Removed {0:^3} from stack".format(stack.pop()))
    stack.add(-99)
    print("Top of stack is :{0}".format(stack.peek()))

    #end of testing
    while stack.peek() is not None : 
        print("Removed {0:^3} from stack".format(stack.pop()))
