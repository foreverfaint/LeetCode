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
        if root.left is None and root.right is None:
            min_ = root.val
            max_ = root.val
            diff = float("inf")
            return min_, max_, diff
        elif root.left is None:
            min_ = root.val
            r_min_, r_max_, diff = self.foo(root.right)
            diff = min(abs(root.val - r_min_), diff)
            return min_, r_max_, diff
        elif root.right is None:
            max_ = root.val
            l_min_, l_max_, diff = self.foo(root.left)
            diff = min(abs(root.val - l_max_), diff)
            return l_min_, max_, diff
        else:
            l_min_, l_max_, l_diff = self.foo(root.left)
            r_min_, r_max_, r_diff = self.foo(root.right)
            diff = min([l_diff, r_diff, abs(root.val - l_max_), abs(root.val - r_min_)])
            return l_min_, r_max_, diff

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_, max_, diff = self.foo(root)
        return diff 


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([4,2,6,1,3])
    print(sln.getMinimumDifference(tree))

    tree = TreeNode.from_list([1,0,48,None,None,12,49])
    print(sln.getMinimumDifference(tree))

    tree = TreeNode.from_list([236,104,701,None,227,None,911])
    print(sln.getMinimumDifference(tree))