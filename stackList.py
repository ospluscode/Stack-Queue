# Implementing Stack using python Lists
# Time and Space complexity of all methods is O(1) - constant

class Stack:
    # create stack
    def __init__(self):
        self.list = []

    # printing as string
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)


    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False


    def push(self, value):
        self.list.append(value)
        return "Element pushed"


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