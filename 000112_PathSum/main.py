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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        elif root.left is None and root.right is None:
            return targetSum == root.val
        elif root.left is None:
            return self.hasPathSum(root.right, targetSum - root.val)
        elif root.right is None:
            return self.hasPathSum(root.left, targetSum - root.val)
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


if __name__ == "__main__":
    sln = Solution()
    print(sln.hasPathSum(TreeNode.from_list([1,2]), 1))
    print(sln.hasPathSum(TreeNode.from_list([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22))
    print(sln.hasPathSum(TreeNode.from_list([1,2,3]), 5))
    print(sln.hasPathSum(TreeNode.from_list([]), 0))