from typing import Optional, Tuple, List


class Node:
    def __init__(self, val=0, next=None, random: "Node" = None):
        self.val = val
        self.next = next
        self.random = random

    def to_list(self) -> List[Tuple[int, int]]:
        nodes = [self]
        it = self
        while it.next:
            nodes.append(it.next)
            it = it.next

        ans = []
        for i, node in enumerate(nodes):
            ans.append((node.val, nodes.index(node.random) if node.random is not None else None))
        return ans

    @classmethod
    def from_list(cls, lst: List[Tuple[int, int]]) -> "Node":
        if lst is None or len(lst) == 0:
            return None
        
        nodes = [(cls(val, None, random)) for val, random in lst]
        for i, node in enumerate(nodes):
            node.random = nodes[node.random] if node.random is not None else None
            node.next = nodes[i + 1] if i < len(nodes) - 1 else None
        return nodes[0]


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        nodes = [head]
        it = head
        while it.next:
            nodes.append(it.next)
            it = it.next

        ans = []
        for _, node in enumerate(nodes):
            ans.append((Node(node.val), nodes.index(node.random) if node.random is not None else None))

        for i, (node, random) in enumerate(ans):
            node.next = ans[i + 1][0] if i < len(ans) - 1 else None
            node.random = ans[random][0] if random is not None else None
        return ans[0][0]


if __name__ == "__main__":
    sln = Solution()

    nodes = Node.from_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
    print(sln.copyRandomList(nodes).to_list())

    nodes = Node.from_list([[1,1],[2,1]])
    print(sln.copyRandomList(nodes).to_list())

    nodes = Node.from_list([[3,None],[3,0],[3,None]])
    print(sln.copyRandomList(nodes).to_list())