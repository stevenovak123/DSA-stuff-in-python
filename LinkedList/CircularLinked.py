class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):

        if self.last != None:
            return self.last

        # allocate memory to the new node and add data to the node
        temp = Node(data)

        # assign last to newNode
        self.last = temp

        # create link to itself
        self.last.next = self.last
        return self.last

    # add node to the front
    def addFront(self, data):

        # check if the list is empty
        if self.last == None:
            return self.addToEmpty(data)

        # allocate memory to the new node and add data to the node
        temp = Node(data)

        # store the address of the current first node in the newNode
        temp.next = self.last.next

        # make newNode as last
        self.last.next = temp

        return self.last

    # add node to the end
    def addEnd(self, data):
        # check if the node is empty
        if self.last == None:
            return self.addToEmpty(data)

        # allocate memory to the new node and add data to the node
        temp = Node(data)

        temp.next = self.last.next
        self.last.next = temp
        self.last = temp

        return self.last

    # insert node after a specific node
    def addAfter(self, data, item):

        # check if the list is empty
        if self.last == None:
            return None

        newNode = Node(data)
        previous = self.last.next
        while previous:

            # if the item is found, place newNode after it
            if previous.data == item:

                # make the next of the current node as the next of newNode
                newNode.next = previous.next

                # put newNode to the next of p
                previous.next = newNode

                if previous == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            previous = previous.next
            if previous == self.last.next:
                print(item, "The given node is not present in the list")
                break

    # delete a node
    def deleteNode(self, last, key):

        # If linked list is empty
        if last == None:
            return

        # If the list contains only a single node
        if (last).data == key and (last).next == last:

            last = None

        temp = last
        d = None

        # if last node is to be deleted
        if (last).data == key:

            # find the node before the last node
            while temp.next != last:
                temp = temp.next

            # point temp node to the next of last i.e. first node
            temp.next = (last).next
            last = temp.next

        # travel to the node to be deleted
        while temp.next != last and temp.next.data != key:
            temp = temp.next

        # if node to be deleted was found
        if temp.next.data == key:
            d = temp.next
            temp.next = d.next

        return last

    def traverse(self):
        if self.last == None:
            print("The list is empty")
            return

        newNode = self.last.next
        while newNode:
            print(newNode.data, end=" ")
            newNode = newNode.next
            if newNode == self.last.next:
                break


# Driver Code
if __name__ == "__main__":

    cll = CircularLinkedList()

    last = cll.addToEmpty(6)
    last = cll.addEnd(8)
    last = cll.addFront(2)
    last = cll.addAfter(10, 2)

    cll.traverse()

    last = cll.deleteNode(last, 8)
    print()
    cll.traverse()
