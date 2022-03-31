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
    def _findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return float("inf")
        elif root.left.val < root.right.val:
            min_l = self._findSecondMinimumValue(root.left)
            return min(root.right.val, min_l)
        elif root.left.val > root.right.val:
            min_r = self._findSecondMinimumValue(root.right)
            return min(root.left.val, min_r)
        else:
            min_l = self._findSecondMinimumValue(root.left)
            min_r = self._findSecondMinimumValue(root.right)
            return min(min_l, min_r)

    
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        val = self._findSecondMinimumValue(root)
        return -1 if val == float("inf") else val


if __name__ == "__main__":
    sln = Solution()

    root = TreeNode.from_list([2,2,5,None,None,5,7])
    print(sln.findSecondMinimumValue(root))

    root = TreeNode.from_list([2,2,2])    
    print(sln.findSecondMinimumValue(root))