# Implements First in, First Out "FIFO" Queue
class Queue:

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
            print("queue is empty")
            return self.elements
        else:
            return self.elements.pop(0)

    def print(self):
        if self.is_empty():
            print("queue is empty")
        else:
            i = 0
            for element in self.elements:
                print(str(i) + "-" + str(element)
                i = i + 1