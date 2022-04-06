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
    def length(self, head):
        return (1 + self.length(head.next)) if head else 0

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        l = self.length(head)
        if l == 1:
            return head

        k = k % l
        if k == 0:
            return head

        i = l - k

        j = 0
        it = head
        while j < i - 1: 
            it = it.next
            j += 1
        new_head = it.next
        it.next = None

        it = new_head
        while it.next:
            it = it.next

        it.next = head
        return new_head


if __name__ == "__main__":
    sln = Solution()

    node = ListNode.from_list([1,2,3,4,5])
    print(sln.rotateRight(node, 2).to_list())

    node = ListNode.from_list([0,1,2])
    print(sln.rotateRight(node, 4).to_list())