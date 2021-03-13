# Use a single list to implement 3 stacks
# Idea is to do [0, n/3) , [n/3, 2n/3), [2n/3, n)


class ThreeStack:
    def __init__(self, stack_size):
        self.number_stacks = 3
        # fixed size list
        self.custom_list = [0] * (stack_size * self.number_stacks)
        # size of stacks
        self.sizes = [0] * self.number_stacks
        self.stack_size = stack_size


    def isFull(self, stack_num):
        if self.sizes[stack_num] == self.stack_size:
            return True
        else:
            return False


    def isEmpty(self, stack_num):
        if self.sizes[stack_num] == 0:
            return True
        else:
            return False


    # top elements index - to use in push and pop
    def indexOfTop(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num]- 1


    def push(self, item, stack_num):
        if self.isFull(stack_num):
            return "Stack is full"
        else:
            self.sizes[stack_num] += 1
            # add to the end of the given stack
            self.custom_list[self.indexOfTop(stack_num)] = item


    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            return "Stack is empty"
        else:
            # top element
            value = self.custom_list[self.indexOfTop(stack_num)]
            self.custom_list[self.indexOfTop(stack_num)] = 0
            self.sizes[stack_num] -= 1
            return value


    def peek(self, stack_num):
        if self.isEmpty(stack_num):
            return "Stack is empty"
        else:
            value = self.custom_list[self.indexOfTop(stack_num)]
            return value