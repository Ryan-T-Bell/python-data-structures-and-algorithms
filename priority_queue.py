# Implements priority queue sorted smallest to largest.
# pop removes lowest cost element
class PriorityQueue:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    # element - Element to insert
    def insert(self, element):
        self.elements.append(element)
        self.elements.sort(reverse=False)
        return self.elements

    def pop(self):
        if self.is_empty():
            print("queue is empty")
            return self.elements
        else:
            return self.elements.pop(0)

    # Replace repeated element in queue if it has a lower path cost
    def replace_repeated_entry(element):
        i = elements.index(element)
        current_value = elements[i]

        elements[i] = min(current_value, element)

        self.elements.sort(reverse=False)

    def print(self):
        if self.is_empty():
            print("queue is empty")
        else:
            i = 0
            for element in self.elements:
                print(str(i) + "-" + str(element))
                i = i + 1