from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __str__(self) -> str:
        s = str(self.val)
        if self.children:
            s += f" (" + ",".join([str(x) for x in self.children]) + ")"
        return s

    @classmethod
    def from_list(cls, lst) -> "Node":
        if not lst:
            return None

        root = cls(lst[0])

        from collections import deque
        q = deque()
        q.append(root)

        i = 1
        while len(q) > 0:
            parent = q.popleft()
            i += 1
            
            children = []
            while i < len(lst) and lst[i] is not None:
                node = cls(lst[i])
                children.append(node)
                q.append(node)
                i += 1

            parent.children = children
        
        return root


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        if not root.children:
            return [root.val]

        ans = []
        for child in root.children:
            ans.extend(self.postorder(child))
        ans.append(root.val)
        return ans


if __name__ == "__main__":
    sln = Solution()

    root = Node.from_list([1,None,3,2,4,None,5,6])
    print(sln.postorder(root))

    root = Node.from_list([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
    print(sln.postorder(root))    