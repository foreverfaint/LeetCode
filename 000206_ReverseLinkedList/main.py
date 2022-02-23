from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, __o: object) -> bool:
        if __o is None:
            return False

        if self.val == __o.val:
            if self.next is None and __o.next is not None:
                return False
            return self.next == __o.next

        return False

    def __str__(self) -> str:
        if self.next is None:
            return str(self.val)
        return str(self.val) + " " + self.next.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_list(cls, lst: List[int]) -> "ListNode":
        r = cls()
        s = r
        for digit in lst:
            s.next = cls(digit)
            s = s.next
        return r.next


class Solution:
    def _reverse_and_return_new_head_and_tail(self, head):
        if not head.next:
            return head, head
        new_head, new_tail = self._reverse_and_return_new_head_and_tail(head.next)
        new_tail.next = head
        head.next = None
        return new_head, head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head, new_tail = self._reverse_and_return_new_head_and_tail(head)
        return new_head


if __name__ == "__main__":
    sln = Solution()
    print(sln.reverseList(ListNode.from_list([1,2,3,4,5])))
    print(sln.reverseList(ListNode.from_list([1,2])))
    print(sln.reverseList(ListNode.from_list([])))