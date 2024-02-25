class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        newNode = Node(val)
        cur = self.head

        for _ in range(index):
            cur = cur.next

        newNode.next = cur.next
        cur.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head
        if index == 0:
            self.head.next = self.head.next.next
        else:
            while index >= 1:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next

        self.size -= 1

# Example usage:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# print(obj.get(1))  # Output: 2
# obj.deleteAtIndex(1)
# print(obj.get(1))  # Output: 3


