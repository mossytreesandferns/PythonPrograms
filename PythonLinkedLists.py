"""Linked Lists"""

# data structures of linked lists are called nodes

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node 

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node=current_node.next
            elements.append(current_node.data)
        print(elements) 

    def get(self, index): #iterate over
        if index >= self.length():
            print("Error: Index out of range") 
            return None
        current_index =0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index: 
                return current_node.data
            current_index += 1   

    def erase(self, index): # erase function  
        if index >= self.length():
            print("Error: Index out of range")
            return
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next 
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1





my_list = linked_list()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()

print("element at second index: %d" % my_list.get(2))
my_list.erase(1)
my_list.display()



"""Double linked lists"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node    
            new_node.prev = cur
            new_node.next = None    
             
    def prepend(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None    

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)   
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next    

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev  
            cur = cur.next    


dLinklist = DoublyLinkedList()
dLinklist.append(1)                      
dLinklist.append(2)
dLinklist.append(3)
dLinklist.append(4)
dLinklist.print_list()

dLinklist.add_before_node(1,111)
dLinklist.add_before_node(2,112)
dLinklist.add_before_node(4,114)

dLinklist.add_after_node(1,11)
dLinklist.add_after_node(2,12)
dLinklist.add_after_node(4,14)
dLinklist.print_list()

dLinklist.prepend(0)
dLinklist.print_list()

dLinklist.prepend(5)
dLinklist.print_list()





