# Implementing Stack using python Lists - max size
# Time and Space complexity of all methods is O(1) - constant

class Stack:
    # maximum size of stack
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False


    # only for stack with max size
    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False


    def push(self, value):
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(value)
            return "Element inserted"


    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()
    

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[len(self.list)-1]


    def delete(self):
        self.list = None