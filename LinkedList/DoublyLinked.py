import gc


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # * insert node at the front
    def insert_front(self, data):

        # * create node and assigning data to the node
        new_node = Node(data)

        # * Make new node the head
        new_node.next = self.head

        # * assign prev to null. Currently constructor assigns it to null

        # * remove the head from the second node and point it to the inserted Node
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insert_after(self, prev_node, data):

        # * check if previous node is null
        if prev_node is None:
            print("previous node cannot be null")
            return

        new_node = Node(data)

        # * set next of newNode to the next of prevNode
        new_node.next = prev_node.next

        # * set next of prev node to newNode
        prev_node.next = new_node

        # *set prev of newNode to the previous node
        new_node.prev = prev_node

        # * set prev of newNode's next to newNode
        if new_node.next:
            new_node.next.prev = new_node

        def insert_end(self, data):
            new_node = Node(data)

            # * if the linked list is empty,make newNode as head
            if self.head is None:
                self.head = new_node
                return

            # * store the head node temporarily
            temp = self.head

            # * if the linked list is not empty, traverse to the end of the linked List
            while temp.next:
                temp = temp.next

            # * assign the next of the last node to the newNode
            temp.next = new_node
