class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delBeg(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = self.tail = None
            return
        elif self.head is not None:
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
            return

    def addNode(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def addNodeAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def printList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()

dll = DoublyLinkedList()
dll.addNode(1)  # Add a node with value 1 to the linked list
dll.addNode(3)  # Add a node with value 2 to the linked list
dll.addNode(5)  # Add a node with value 2 to the linked list
dll.addNode(7)  # Add a node with value 2 to the linked list
dll.addNode(9)  # Add a node with value 2 to the linked list
dll.addNodeAtEnd(10)
dll.addNodeAtEnd(15)
dll.printList()
dll.delBeg()
# Print the values of nodes in linked list after deletion by iterating through all nodes starting from head
current_node = dll.head
values = []
while current_node is not None :
    values.append(current_node.value)
    current_node = current_node.next

print(values)