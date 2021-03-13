# Queue implementation using Linked List
# Simply adding a new node to linked list as a next node
# when we are adding a new element to the queue
# And for dequeue we remove first node from linked list
# All TC and SC is O(1) - constant

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()
    
    def __str__(self):
        values = [str(l) for l in self.linked_list]
        return ' '.join(values)


    def enqueue(self, value):
        new_node = Node(value)
        # if its first node
        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node


    def isEmpty(self):
        # if head is empty it means the linked list is empty
        if self.linked_list.head == None:
            return True
        else:
            return False


    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            temp_node = self.linked_list.head
            # if there is only 1 node
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                # assign head to the second node
                self.linked_list.head = self.linked_list.head.next
            return temp_node


    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.linked_list.head


    def delete(self):
        # garbage collector removes all nodes
        # once the head and tail links are removed
        self.linked_list.head = None
        self.linked_list.tail = None