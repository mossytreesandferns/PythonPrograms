# Lucid Programmign on Youtube

"""Stacks: LIFO"""

class Stack():
    def __init__(self): # modifies python list
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []   

    def peek(self): # tells top most element
        if not self.is_empty():
            return self.items[-1] 

    def get_stack(self): 
        return self.items
s = Stack()
# s.push("A")
# s.push('B')
# print(s.get_stack())   
# s.push('C')
# print(s.get_stack())
# s.pop() 
# print(s.get_stack())  
# print(s.is_empty()) 
# print(s.peek()) 
print()

# Solving problem: is a set of parentheses balanced or not?
def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True 
    else:
        return False   

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

        if s.is_empty() and is_balanced:
            return True
        else:
            return False                    

print(is_paren_balanced("[]"))

# Convert integar value to binary
def div_by_2(dec_num):
    s = Stack()

    while dec_num>0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num//2

    bin_num = ""
    while not s.is_empty(): 
        bin_num+= str(s.pop())
    return bin_num

print(div_by_2(242))


"""Queues: FIFO"""
# Just a list where data goes in at the end and comes out at the begining
queue_example = ["Mercury", "Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Kuiper Belt"]
class queue:
    def __init__(self,queue):
        self.queue = queue

    # View items in queue
    def view(self,queue):
        for item in range(len(self.queue)):
            print(self.queue[item])

    # Push items onto queue
    def push(self, item, queue):
        self.queue.append(item)
        return self.queue

    # Pop items out of queue
    def pop(self,queue):
        self.item=self.queue.pop(0)
        return self.item, self.queue


queue1 = queue(queue_example)

queue1.view(queue_example) 
print(queue1.push("Oort Cloud",queue_example)) 
print(queue1.pop(queue_example))    