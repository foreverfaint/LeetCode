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
    def from_list(cls, lst: List[int], pos: int = -1) -> "ListNode":
        r = cls()
        s = r
        for digit in lst:
            s.next = cls(digit)
            s = s.next
        
        if pos == -1:
            return r
        
        head = r.next
        curr = head
        loop = None
        i = 0
        while True:
            if i == pos:
                loop = curr
            i += 1
            if curr.next != None:
                curr = curr.next
            else:
                curr.next = loop
                break
        return head


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        while p1 is not None and p2 is not None:
            p1 = p1.next
            p2 = p2.next
            if p2 is None:
                return False
            p2 = p2.next
            if id(p1) == id(p2):
                return True
        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.hasCycle(ListNode.from_list([3,2,0,-4], 1)))
    print(sln.hasCycle(ListNode.from_list([3,2,0,-4], -1)))
    print(sln.hasCycle(ListNode.from_list([1, 2], 0)))