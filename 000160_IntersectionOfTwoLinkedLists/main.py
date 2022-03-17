from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self) -> List[int]:
        if self.next is None:
            return []
        return [self.val] + self.next.to_list()

    @classmethod
    def from_list(cls, lst: List[int]) -> "ListNode":
        if lst is None or len(lst) == 0:
            return None
        return ListNode(lst[0], cls.from_list(lst[1:]))


def join(intersectVal, headA, headB, skipA, skipB):
    if intersectVal > 0:
        cursorA = headA
        while skipA > 1:
            cursorA = cursorA.next
            skipA -= 1
            
        cursorB = headB
        while skipB > 1:
            cursorB = cursorB.next
            skipB -= 1

        cursorB.next = cursorA.next
    return headA, headB


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer = set()

        cursorA = headA
        while cursorA != None:
            pointer.add(cursorA)
            cursorA = cursorA.next

        cursorB = headB
        while cursorB != None:
            if cursorB in pointer:
                return cursorB
            cursorB = cursorB.next
        
        return None


if __name__ == "__main__":
    sln = Solution()

    input = join(8, ListNode.from_list([4,1,8,4,5]), ListNode.from_list([5,6,1,8,4,5]), 2, 3)
    print(sln.getIntersectionNode(*input).val)

    input = join(2, ListNode.from_list([1,9,1,2,4]), ListNode.from_list([3,2,4]), 3, 1)
    print(sln.getIntersectionNode(*input).val)

    input = join(0, ListNode.from_list([2,6,4]), ListNode.from_list([1,5]), 3, 2)
    print(sln.getIntersectionNode(*input))