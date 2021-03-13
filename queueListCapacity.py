# Queue with capacity / maximum size (Circular Queue) implementation using Py List
# Enqueue and Dequeue TC is O(n), rest is O(1) as well as SC of all
# Circular Queue happens to prevent unused memory allocation
# All TC and SC is O(1) - constant


class Queue:
    def __init__(self, max_size):
        # init empty list with None values
        self.list = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1 
    
    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)


    def isFull(self):
        # top circles and reaches to start
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False


    def isEmpty(self):
        # top has no value
        if self.top == -1:
            return True
        else:
            return False


    # insert/push
    def enqueue(self, value):
        if self.isFull():
            return "Queue is full"
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value
            return "Element inserted"


    # remove/pop
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            first_element = self.list[self.start]
            start = self.start
            # if only element in queue
            if self.start == self.top:
                self.start = -1
                self.top = -1
            # if last element
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            # set its place to none
            self.list[start] = None
            return first_element


    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list[self.start]


    def delete(self):
        self.list = self.max_size * [None]
        self.top = -1
        self.start = -1