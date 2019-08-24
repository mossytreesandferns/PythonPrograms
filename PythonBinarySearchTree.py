"""Binary Search Tree and Binary Search Tree"""

# space O(n), time avg worst O(nlogn) O(n)


class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            self._insert(data,self.root) 

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left == None:
                current_node.left = node(data)
            else:
                self._insert(data,current_node.left) 
        elif data > current_node.data:
            if current_node.right == None:
                current_node.right = node(data)
            else: 
                self._insert(data, current_node.right)
        else:
            print("Value is already in tree.")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)   

    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left)
            print(str(current_node.data))
            self._print_tree(current_node.right)  

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None:
            return current_height
        left_height = self._height(current_node.left, current_height + 1)
        right_height = self._height(current_node.right, current_height + 1)
        return max(left_height,right_height)   

    def search(self,data):
        if self.root != None:
            return self._search(data, self.root)
        else:
            return False 

    def _search(self,data,current_node):
        if data ==current_node.data:
            return True
        elif data < current_node.data and current_node.left != None:
            return self._search(data,current_node.left)   
        elif data > current_node.data and current_node.right != None:
            return self._search(data,current_node.right)  
        return False


tree = binary_search_tree()
tree.insert(3)
tree.insert(2)
tree.insert(5)
tree.insert(8)
tree.insert(1)
tree.insert(4)
tree.insert(30)
tree.insert(22)
tree.insert(17)
tree.insert(14)
tree.insert(7)

tree.print_tree()

print(tree.height())
print(tree.search(29))
print(tree.search(17))


