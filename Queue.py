class Node : 
    def __init__(self , value ) : 
        self.value = value 
        self.next = None 

class Queue : 
    def __init__(self) : 
        self.head = None
        self.tail = None 
        self.length = 0 

    def add(self, value ): 
        newNode = Node(value )
        if self.head is None : 
            self.head = self.tail = newNode
            
        else : 
            self.tail.next = newNode
            self.tail = newNode
        self.length +=1
        
    def remove(self ) : 
        if self.head is not None  : 
            
            removedHead = self.head
            self.head = self.head.next 
            if self.head is None : 
                self.tail = None 

            self.length -=1 
            return removedHead.value
        
        return None
        
    def size(self) : 
        return self.length
    def is_empty(self) : 
        return self.head is None and self.tail is None

if __name__ == "__main__":
    new_queue = Queue()
    for i in range(10):
        new_queue.add(i)
    for i in range(5): 
        print("Removed value : {0}".format(new_queue.remove()))
        print("Size of Queue: {0}".format(new_queue.size()))
        print()
    
    for i in range(98,90,-1) : 
        new_queue.add(i) 
    print()
    print("After adding a few more nodes the size is {0}".format(new_queue.size()))
    while not new_queue.is_empty() : 
        print("Removed value : {0}".format(new_queue.remove()))
        print("Size of Queue: {0}".format(new_queue.size())) 
        print()