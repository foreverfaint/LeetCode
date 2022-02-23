
from typing import Optional, Tuple, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def lst_2_node(lst: List[int]):
    if len(lst) == 0:
        return None

    node = ListNode(lst[0], None)
    node.next = lst_2_node(lst[1:])
    return node


def node_2_lst(head: ListNode) -> List[int]:
    if head is None:
        return []
    return [head.val] + node_2_lst(head.next)





class Solution:
    def len_node(self, head: ListNode):
        if head is None:
            return 0

        i = 1
        while head.next:
            i += 1
            head = head.next
        return i

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = self.len_node(head)
        if count == 1 and n == 1:
            return None

        passed = count - n
        if passed == 0:
            return head.next

        node = head
        while passed > 1:
            node = node.next
            passed -= 1
        node.next = node.next.next
        return head


if __name__ == "__main__":
    sln = Solution()
    print(node_2_lst(sln.removeNthFromEnd(lst_2_node([1,2,3,4,5]), 2)))
    print(node_2_lst(sln.removeNthFromEnd(lst_2_node([1]), 1)))
    print(node_2_lst(sln.removeNthFromEnd(lst_2_node([1, 2]), 1)))
    print(node_2_lst(sln.removeNthFromEnd(lst_2_node([1, 2]), 2)))
    print(node_2_lst(sln.removeNthFromEnd(lst_2_node([1, 2, 3]), 2)))
        