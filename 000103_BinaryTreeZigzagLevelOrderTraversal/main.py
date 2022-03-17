from typing import List, Optional

from numpy import empty


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.val}{' L(' + str(self.left) + ')' if self.left else ''}{' R(' + str(self.right) + ')'  if self.right else ''}"

    def __repr__(self) -> str:
        return self.__str__()

    def to_list(self):
        return [self.val] + (self.left.as_list() if self.left else []) + (self.right.as_list() if self.right else [])

    @classmethod
    def from_list(cls, lst) -> "TreeNode":
        l = len(lst)
        if l == 0:
            return None

        root = cls(lst[0])
        i = 1
        import queue
        q = queue.Queue()
        q.put_nowait(root)
        while not q.empty():
            r = q.get_nowait()

            if i < l and lst[i]:
                r.left = cls(lst[i])
                q.put_nowait(r.left)

            i += 1
            if i < l and lst[i]:
                r.right = cls(lst[i])
                q.put_nowait(r.right)

            i += 1

        return root


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        from collections import deque
        queue = deque()
        queue.append((root, 0))

        arr = []
        pre_lvl = 0
        while len(queue) > 0:
            first, lvl = queue.popleft()
            if pre_lvl != lvl:
                if pre_lvl % 2 == 1:
                    arr.reverse()
                result.append(arr)
                arr = []
                pre_lvl = lvl

            arr.append(first.val)

            if first.left:
                queue.append((first.left, lvl + 1))
            
            if first.right:
                queue.append((first.right, lvl + 1))

        if pre_lvl % 2 == 1:
            arr.reverse()
        result.append(arr)

        return result


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([3,9,20,None,None,15,7])
    print(sln.zigzagLevelOrder(tree))

    tree = TreeNode.from_list([1])
    print(sln.zigzagLevelOrder(tree))

    tree = TreeNode.from_list([])
    print(sln.zigzagLevelOrder(tree))