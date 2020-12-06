
# Implements Stack AKA Last in, First Out "LIFO" Queue
class Stack():

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def insert(self, element):
        self.elements.append(element)
        return self.elements

    def pop(self):
        if self.is_empty():
        	print("stack is empty")
        	return self.elements
        else:
        	return self.elements.pop(-1)

    def print(self):
        if self.is_empty():
            print("stack is empty")
        else:
            i = 0
            for element in self.elements:
                print(str(i) + "-" + str(element))
                i = i + 1