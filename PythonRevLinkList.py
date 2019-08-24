class node:
    def __init__(self, data):
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
            if current_index == index: return current_node.data
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

    def reverse_list(self,head):                
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev    