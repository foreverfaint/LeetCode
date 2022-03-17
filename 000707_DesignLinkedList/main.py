class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} {self.next}" if self.next else str(self.val)

    @classmethod
    def add(cls, val, next = None):
        return cls(val, next)

class MyLinkedList:
    def __init__(self):
        self._head = ListNode(-1)
        
    def get(self, index: int) -> int:
        node = self._head
        while index >= 0:
            node = node.next
            if not node:
                return -1
            index -= 1
        return node.val
        
    def addAtHead(self, val: int) -> None:
        self._head.next = ListNode(val, self._head.next)

    def addAtTail(self, val: int) -> None:
        node = self._head
        while node.next:
            node = node.next
        node.next = ListNode(val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        node = self._head
        while index > 0:
            node = node.next
            if not node:
                return
            index -= 1
        node.next = ListNode(val, node.next)
        
    def deleteAtIndex(self, index: int) -> None:
        node = self._head
        while index > 0:
            node = node.next
            if not node:
                return
            index -= 1
        
        if node.next:
            node.next = node.next.next

    def __str__(self) -> str:
        return str(self._head)


if __name__ == "__main__":
    a = MyLinkedList()
    a.addAtIndex(0, 10)
    a.addAtIndex(0, 20)
    a.addAtIndex(0, 30)
    print(a)
    print(a.get(0))

        