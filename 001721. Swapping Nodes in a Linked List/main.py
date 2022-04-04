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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = []
        ans.append(head)
        it = head
        while it.next:
            ans.append(it.next)
            it = it.next

        t = ans[k - 1].val
        ans[k - 1].val = ans[-k].val
        ans[-k].val = t
        return head


if __name__ == "__main__":
    sln = Solution()

    nodes = ListNode.from_list([1,2,3,4,5])
    print(sln.swapNodes(nodes, 2).to_list())

    nodes = ListNode.from_list([7,9,6,6,7,8,3,0,9,5])
    print(sln.swapNodes(nodes, 5).to_list())    