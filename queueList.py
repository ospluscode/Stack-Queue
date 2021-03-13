# Queue implementation using Py List
# Enqueue and Dequeue TC is O(n), rest is O(1) as well as SC of all

class Queue:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = [str(l) for l in self.list]
        return ' '.join(values)


    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False


    # insert/push method
    def enqueue(self, value):
        self.list.append(value)
        return "Element inserted"


    # remove/pop method
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list.pop(0)


    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list[0]


    def delete(self):
        self.list = None