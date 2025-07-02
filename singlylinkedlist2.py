class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node


    def deleteFromBeginning(self):

        # Linked list is empty
        if self.head is None:
            return

        self.head = self.head.next

    # Deleting from end -> Method 1
    def deleteFromEnd(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Deleting from end -> Method 2
    def deleteFromTheEnd(self):
        prev = self.head
        curr = self.head.next

        while curr.next:
            prev = curr
            curr = curr.next

        prev.next = None


    def printLinkedList(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


if __name__ == "__main__":
    llist = LinkedList()

    print("\nInserting at the beginning...")
    llist.insertAtBeginning("fox")
    llist.insertAtBeginning("brown")
    llist.insertAtBeginning("quick")
    llist.insertAtBeginning("The")
    llist.printLinkedList()

    print("\nInserting at the end...")
    llist.insertAtEnd("jumps")
    llist.printLinkedList()

    print("\nDeleting from the end...")
    llist.deleteFromTheEnd()
    llist.printLinkedList()

    print("\nDeleting from the beginning...")
    llist.deleteFromBeginning()
    llist.printLinkedList()

    print()
    llist.insertAtBeginning("A")
    llist.printLinkedList()
