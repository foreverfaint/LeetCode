from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self) -> List[int]:
        if self.next is None:
            return [self.val]
        return [self.val] + self.next.to_list()

    @classmethod
    def from_list(cls, lst: List[int]) -> "ListNode":
        if lst is None or len(lst) == 0:
            return None
        return ListNode(lst[0], cls.from_list(lst[1:]))


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        while True:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None
                break


if __name__ == "__main__":
    sln = Solution()

    head = ListNode.from_list([4,5,1,9])
    sln.deleteNode(head.next)
    print(head.to_list())

    head = ListNode.from_list([4,5,1,9])
    sln.deleteNode(head.next.next)
    print(head.to_list())