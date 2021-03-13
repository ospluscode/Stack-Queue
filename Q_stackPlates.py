# Implement a stack that is identical to stack of plates
# When a stack reach to a capacity push the new element to a new stack
# that is continuation of the previous stack

class StackPlates():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def __str__(self):
        return self.stacks


    def push(self, item):
        # if there is space add it to the end
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            # because its 2 dimensional list
            self.stacks.append([item])


    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()


    def pop_at(self, stack_num):
        if len(self.stacks[stack_num]) > 0:
            return self.stacks[stack_num].pop()
        else:
            return None