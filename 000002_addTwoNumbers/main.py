from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: "ListNode" = next

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode()
        s = r
        carry = 0
        
        while l1 and l2:
            val = (l1.val + l2.val + carry)
            carry = val // 10
            s.next = ListNode(val % 10)
            l1 = l1.next
            l2 = l2.next
            s = s.next
            
        while l1:
            val = (l1.val + carry)
            carry = val // 10
            s.next = ListNode(val % 10)
            l1 = l1.next
            s = s.next
            
        while l2:
            val = (l2.val + carry)
            carry = val // 10
            s.next = ListNode(val % 10)
            l2 = l2.next
            s = s.next
            
        if carry > 0:
            s.next = ListNode(carry)
        
        return r.next



def l2n(lst: List[int]) -> ListNode:
    r = ListNode()
    s = r
    for digit in lst:
        s.next = ListNode(digit)
        s = s.next
    return r.next


if __name__ == "__main__":
    assert "1 2" == str(ListNode.from_list([1, 2]))
    assert ListNode.from_list([1, 2]) == ListNode.from_list([1, 2])
    assert ListNode.from_list([7,0,8]) == Solution().addTwoNumbers(ListNode.from_list([2,4,3]), ListNode.from_list([5,6,4]))
    assert ListNode.from_list([0]) == Solution().addTwoNumbers(ListNode.from_list([0]), ListNode.from_list([0]))
    assert ListNode.from_list([8,9,9,9,0,0,0,1]) == Solution().addTwoNumbers(ListNode.from_list([9,9,9,9,9,9,9]), ListNode.from_list([9,9,9,9]))
            