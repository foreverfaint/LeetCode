from typing import Optional, List


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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 != None and list2 != None:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
        elif list1 != None:
            return list1
        else:
            return list2


if __name__ == "__main__":
    print(node_2_lst(Solution().mergeTwoLists(lst_2_node([1,2,4]), lst_2_node([1,3,4]))))
    print(node_2_lst(Solution().mergeTwoLists(lst_2_node([]), lst_2_node([]))))
    print(node_2_lst(Solution().mergeTwoLists(lst_2_node([]), lst_2_node([1,3,4]))))
    print(node_2_lst(Solution().mergeTwoLists(lst_2_node([1,2,4]), lst_2_node([]))))