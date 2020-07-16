class Node : 
    
    def __init__(self,value ) : 
        self.value = value 
        self.next = None 

class List: 
    

    def __init__(self) : 
        self.length = 0 
        self.head = None 
        self.tail = None

    def insert(self,value ,  i = -1) : 
        node = Node(value)
        #base case empty list 
        if self.tail is None and self.head is None : 
            self.tail = self.head = node 
            return True
        #by default append 
        if i == -1 : 
            self.tail.next = node 
            self.tail = node 
        elif i == 0 : 

            node.next = self.head 
            self.head = node 
        else : 
            j = 0 
            current = self.head 
            while j < i and current is not None : 
                j +=1 
                current = current.next             
            if current is None  :  # couldnt find target index aka index out of range. Could throw error here. 
                 return False 
            node.next = current.next 
            current.next = node  
        return True

    def remove(self, i = 0 ) : 
        if i == 0 : 
            temp = self.head 
            self.head = self.head.next()
            return self.head 
        else : 
            j = 0 
            current = self.head 
            while j < i and  current is not None :
                j +=1 
                current =current.next 
            if current is None : 
                return None 
            else : 
                temp = current 
                current = current.next 
                return temp 

    def k_last(self,k):
        #base case , k = 0 
        if k == 0 : 
            return None 
        #if n is known you can find the n-kth first element. 
        # Because its a linked list assume n is not known
        #Note : 
        #k is guaranteed to be smaller than the length of the list. 
        #The list is very long, so making more than one pass is prohibitively expensive.
        current = self.head 
        k_element = None 
        i = 1 

        while current is not None : 
            if i == k and k_element is None: 
                k_element = self.head 
                i-=1 
            elif i == k : 
                k_element = k_element.next 
                i -=1 

            i +=1 
            current = current.next

        if k_element is None : 
            return None 
        else : 
            return k_element.value


if __name__ == "__main__" : 
    linked_list = List()
    for i in range(1,11): 
        linked_list.insert(i)
    
    current  = linked_list.head
    while current is not None : 
        print("{0}".format(current.value), end= ",")
        current = current.next 
    print()
    print("\nForgot 0, adding it in now ...")
    linked_list.insert(0,0)
    print("Sucessfully Added Zero. Heres the list now: ")
    current = linked_list.head
    while current is not None : 
        print("{0}".format(current.value), end= ",")
        current = current.next 
    
    k=1
    print()
    print("The {0}th last element is {1}".format(k,linked_list.k_last(k)))

