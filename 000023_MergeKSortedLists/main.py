
from typing import List, Optional, Tuple
import heapq
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [x for x in lists if x is not None]
        if not lists:
            return None

        head = ListNode(-1)
        curr = head            

        # init heap
        heap = []
        for i, x in enumerate(lists):
            heapq.heappush(heap, (x.val, i))

        while heap:
            _, i = heapq.heappop(heap)

            curr.next = lists[i]
            curr = curr.next
            lists[i] = lists[i].next
            curr.next = None

            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        return head.next



if __name__ == "__main__":
    sln = Solution()
    print(node_2_lst(sln.mergeKLists([lst_2_node(x) for x in [[1,4,5],[1,3,4],[2,6]]])))
    print(node_2_lst(sln.mergeKLists([lst_2_node(x) for x in [[1],[4],[5],[1],[3],[4],[2],[6]]])))
    print(node_2_lst(sln.mergeKLists([lst_2_node(x) for x in []])))
    print(node_2_lst(sln.mergeKLists([lst_2_node(x) for x in [[]]])))