"""Graphs: Also Known as Adjacency Lists"""

dictionary = {}

class graph:

    def __init__(self,dct):
        self.dct = dct

    def add_key_value(self,dct,key,value):
        self.dct[key] = value
        return self.dct

    def get_dct(self, dct):
        return dct

    def get_value(self, dct, index):
        return dct[index]  

graph1 = graph(dictionary)

graph1.add_key_value(dictionary,0,[1,2])
graph1.add_key_value(dictionary,1,[2,3])
graph1.add_key_value(dictionary,2,[4,5])
graph1.add_key_value(dictionary,3,[4,5])
graph1.add_key_value(dictionary,4,[6,7])
graph1.add_key_value(dictionary,5,[0,4])

print(graph1.get_dct(dictionary))
print(graph1.get_value(dictionary,4))