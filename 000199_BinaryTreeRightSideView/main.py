
from typing import List, Optional


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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []

        from queue import Queue
        q = Queue()
        q.put_nowait((root, 0))

        last_val = -1
        last_lvl = -1
        while not q.empty():
            first, lvl = q.get_nowait()
            if lvl != last_lvl:
                ans.append(last_val)

            last_val = first.val
            last_lvl = lvl

            if first.left:
                q.put_nowait((first.left, lvl + 1))
            if first.right:
                q.put_nowait((first.right, lvl + 1))

        ans.append(last_val)
        return ans[1:]


if __name__ == "__main__":
    sln = Solution()

    root = TreeNode.from_list([1,2,3,4])
    print(sln.rightSideView(root))

    root = TreeNode.from_list([1,2,3,None,5,None,4])
    print(sln.rightSideView(root))

    root = TreeNode.from_list([1,None,3])
    print(sln.rightSideView(root))

    root = TreeNode.from_list([])
    print(sln.rightSideView(root))