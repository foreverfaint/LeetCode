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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        data = []
        while head.next:
            data.append(head.val)
            head = head.next
        data.append(head.val)

        i = 0
        j = len(data) - 1
        while i < j:
            if data[i] != data[j]:
                return False
            i += 1
            j -= 1
        return True



if __name__ == "__main__":
    sln = Solution()
    print(sln.isPalindrome(ListNode.from_list([1,2,2,1])))
    print(sln.isPalindrome(ListNode.from_list([1,2])))