from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}{(',' + str(self.next)) if self.next else ''}"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_list(cls, lst):
        return cls(lst[0], cls.from_list(lst[1:])) if lst else None


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = k
        curr = head
        while i > 0:
            if not curr:
                return head
            curr = curr.next
            i -= 1

        i = k
        new_head = None
        new_tail = head
        old_head = head
        while i > 0:
            t = old_head.next
            old_head.next = new_head
            new_head = old_head
            old_head = t
            i -= 1

        new_tail.next = self.reverseKGroup(old_head, k)
        return new_head


if __name__ == "__main__":
    sln = Solution()
    print(sln.reverseKGroup(ListNode.from_list([1,2,3,4,5]), 2))
    print(sln.reverseKGroup(ListNode.from_list([1,2,3,4,5]), 3))
    print(sln.reverseKGroup(ListNode.from_list([1,2,3,4,5,6,7,8,9]), 3))
    print(sln.reverseKGroup(ListNode.from_list([1,2,3,4,5,6,7,8,9,10]), 3))