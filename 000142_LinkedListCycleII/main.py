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


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        while head != None:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None


def cyclize(head, pos):
    if pos != -1:
        cursor = head
        i = 0
        pos_pointer = None
        while cursor.next != None:
            if i == pos:
                pos_pointer = cursor
            i += 1
            cursor = cursor.next
        cursor.next = pos_pointer
    return head


if __name__ == "__main__":
    sln = Solution()

    input = cyclize(ListNode.from_list([3,2,0,-4]), 1)
    print(sln.detectCycle(input))

    input = cyclize(ListNode.from_list([1,2]), 0)
    print(sln.detectCycle(input))

    input = cyclize(ListNode.from_list([1]), -1)
    print(sln.detectCycle(input))