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
    def from_list(cls, lst: List[int]) -> Optional["ListNode"]:
        r = cls()
        s = r
        for digit in lst:
            s.next = cls(digit)
            s = s.next
        return r.next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        n = head
        while n:
            l += 1
            n = n.next

        i = 1
        m = (l // 2) + 1
        while i < m:
            head = head.next
            i += 1

        return head


if __name__ == "__main__":
    sln = Solution()
    print(sln.middleNode(ListNode.from_list([1])))
    print(sln.middleNode(ListNode.from_list([1,2])))
    print(sln.middleNode(ListNode.from_list([1,2,3,4,5])))
    print(sln.middleNode(ListNode.from_list([1,2,3,4,5,6])))