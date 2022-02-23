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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if head and not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(head.next.next)
        new_head.next = head
        return new_head


if __name__ == "__main__":
    sln = Solution()
    print(sln.swapPairs(ListNode.from_list([1,2,3,4])))
    print(sln.swapPairs(ListNode.from_list([])))
    print(sln.swapPairs(ListNode.from_list([1])))