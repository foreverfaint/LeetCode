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
    def reverse(self, node):
        if not node.next:
            return node, node

        head, tail = self.reverse(node.next)
        tail.next = node
        node.next = None
        return head, node

    def _addTwoNumbers(self, l1, l2, carry):
        if not l1 and not l2:
            return ListNode(1, None) if carry else None
        elif not l1:
            val, carry = (l2.val + 1) % 10 if carry else l2.val, l2.val + 1 > 9 if carry else False
            return ListNode(val, self._addTwoNumbers(l1, l2.next, carry))
        elif not l2:
            val, carry = (l1.val + 1) % 10 if carry else l1.val, l1.val + 1 > 9 if carry else False
            return ListNode(val, self._addTwoNumbers(l1.next, l2, carry))
        else:
            val = (l1.val + l2.val + 1) if carry else (l1.val + l2.val)
            val, carry = val % 10, val > 9
            return ListNode(val, self._addTwoNumbers(l1.next, l2.next, carry))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        l1_ = self.reverse(l1)[0]
        l2_ = self.reverse(l2)[0]
        sum_ = self._addTwoNumbers(l1_, l2_, False)
        return self.reverse(sum_)[0]


if __name__ == "__main__":
    sln = Solution()

    l1 = ListNode.from_list([7,2,4,3])
    l2 = ListNode.from_list([5,6,4])
    print(sln.addTwoNumbers(l1, l2).to_list())

    l1 = ListNode.from_list([2,4,3])
    l2 = ListNode.from_list([5,6,4])
    print(sln.addTwoNumbers(l1, l2).to_list())

    l1 = ListNode.from_list([0])
    l2 = ListNode.from_list([0])
    print(sln.addTwoNumbers(l1, l2).to_list())        