"""Implement Singly and Double Linked Lists from imported module"""

from PythonLinkedLists import node, linked_list, Node, DoublyLinkedList

dict1 = {1:"This",2:"is",3:"a",4:"dictionary",5:"of",6:"words"}
dict2 = {"one":1,"two":2,"three":3,"four":4,"five":5}
dict3 = {"house":"cob","apartment":"2 bedroom","condo":"one story","commune":"farmhouse"}
dict4 = {"insect":"dragonfly","conifer":"cycad","gas":"oxygen","amphibian":"amphibian"}
dict5 = {"bacteria":"engulphing","algae":"making","fungi":"absorbing","animals":"ingesting"}

# Implement Singly Linked List
ll_dictions = linked_list()
ll_dictions.display()
ll_dictions.append(dict1)
ll_dictions.append(dict2)
ll_dictions.append(dict3)
ll_dictions.append(dict4)
ll_dictions.append(dict5)
ll_dictions.display()
print(ll_dictions.get(2))
ll_dictions.erase(1)
ll_dictions.display()

#Implement Double Linked List
dll_dictions = DoublyLinkedList()
dll_dictions.append(dict1)
dll_dictions.prepend(dict2)
dll_dictions.add_after_node(dict2,dict3)
dll_dictions.add_before_node(dict3,dict4)
dll_dictions.append(dict5)
dll_dictions.print_list()




