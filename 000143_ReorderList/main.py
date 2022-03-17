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
    def reverse(self, head):
        if head.next is None:
            return head, head
        new_head, new_tail = self.reverse(head.next)
        new_tail.next = head
        head.next = None
        return new_head, head

    def merge(self, head1, head2):
        if head1 is not None:
            head1.next = self.merge(head2, head1.next)
            return head1
        return None

    def count(self, head):
        i = 0
        while head:
            head = head.next
            i += 1
        return i

    def split(self, head, pos):
        cursor = head
        while pos > 1:
            cursor = cursor.next
            pos -= 1

        new_head = cursor.next
        cursor.next = None
        return head, new_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        n = self.count(head)
        print(n)
        import math
        h1, h2 = self.split(head, math.ceil(n / 2))
        # print(h1.to_list(), h2.to_list(), h1, head)
        h2, _ = self.reverse(h2)
        print(h2.to_list(), h1, head)
        h = self.merge(h1, h2)
        print(h.to_list(), h, head)

if __name__ == "__main__":
    sln = Solution()

    # i = ListNode.from_list([1])
    # print(i.to_list())
    # h, t = sln.reverse(i)
    # print(h.to_list())

    # i = ListNode.from_list([1, 2, 3])
    # j = ListNode.from_list([5, 4])
    # h1, h2 = sln.split(j, 1)
    # print(h1.to_list())
    # print(h2.to_list())
    # print(sln.merge(i, j).to_list())
    # print(sln.count(j))

    input = ListNode.from_list([1])
    sln.reorderList(input)
    print(input.to_list())
