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

    def as_list(self):
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
    def _f(self, root):
        if root.left is None and root.right is None:
            return [root.val]
        elif root.left is None:
            return [root.val] + self._f(root.right)
        elif root.right is None:
            return self._f(root.left) + [root.val]
        else:
            return self._f(root.left) + [root.val] + self._f(root.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False

        nums = self._f(root)
        i = 0
        j = len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if k == s:
                return True
            elif k < s:
                j -= 1
            else:
                i += 1
        return False
            

if __name__ == "__main__":
    sln = Solution()
    print(sln.findTarget(TreeNode.from_list([2,None,3]), 6))
    print(sln.findTarget(TreeNode.from_list([1]), 2))
    print(sln.findTarget(TreeNode.from_list([2,1,3]), 3))
    print(sln.findTarget(TreeNode.from_list([5,3,6,2,4,None,7]), 9))
    print(sln.findTarget(TreeNode.from_list([5,3,6,2,4,None,7]), 28))