class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
        self.prev = None
        
        
        
class DoublyLinkedList:
    
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def add(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
        
        
    def remove(self,value):
        currant = self.head
        while currant is not None:
            if currant.value == value:
                if currant.prev is not None:
                    currant.prev.next = currant.next
                else:
                    self.head = currant.next
                if currant.next is not None:
                    currant.next.prev = currant.prev
                else:
                    self.tail = currant.prev
                self.size -= 1
                return
            currant = currant.next
        
        
    
    def search(self,value):
        currant = self.head
        while currant is not None:
            if currant.value == value:
                return True
            currant = currant.next
        return False 
        
    
        
        
    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

dll = DoublyLinkedList()
dll.add(10)
dll.add(5)
dll.add(1)
dll.add(20)
dll.add(3)
dll.display()
 
dll.search( "True", 20)