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
        ans = []
        from queue import Queue
        q = Queue()
        q.put_nowait(self)
        while not q.empty():
            first = q.get_nowait()
            if not first:
                ans.append(None)    
                continue

            ans.append(first.val)
            q.put_nowait(first.left)
            q.put_nowait(first.right)

        return ans

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

            if i < l and lst[i] is not None:
                r.left = cls(lst[i])
                q.put_nowait(r.left)

            i += 1
            if i < l and lst[i] is not None:
                r.right = cls(lst[i])
                q.put_nowait(r.right)

            i += 1

        return root


class Solution:
    def foo(self, root):
        min_diff = float("inf")

        if root.left is None and root.right is None:
            return root.val, root.val, min_diff

        l_min = root.val
        if root.left is not None:
            l_min, l_max, l_min_diff = self.foo(root.left)
            min_diff = min([l_min_diff, min_diff, root.val - l_max])
    
        r_max = root.val
        if root.right is not None:
            r_min, r_max, r_min_diff = self.foo(root.right)
            min_diff = min([r_min_diff, min_diff, r_min - root.val])

        return l_min, r_max, min_diff


    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        _, _, min_ = self.foo(root)
        return min_


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([4,2,6,1,3])
    print(sln.minDiffInBST(tree))

    tree = TreeNode.from_list([1,0,48,None,None,12,49])
    print(sln.minDiffInBST(tree))

    tree = TreeNode.from_list([90,69,None,49,89,None,52])
    print(sln.minDiffInBST(tree))