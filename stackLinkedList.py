# Stack implementation using LinkedList
# Simply, the idea is to insert a node to the head of LinkedList
# each time we push an element to the Stack
# All Time and Space complexity O(1)

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()
    
    def __str__(self):
        values = [str(v.value) for v in self.linked_list]
        return '\n'.join(values)


    def isEmpty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False


    # add node to the head/first
    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node


    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            node_value = self.linked_list.head.value
            return node_value


    # get the head/first node
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            node_value = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return node_value


    def delete(self):
        self.linked_list.head = None