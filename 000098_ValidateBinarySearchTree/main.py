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
        l_is_valid, l_min_, l_max_ = True, root.val, root.val
        if root.left is not None:
            l_min_, l_max_, l_is_valid = self._f(root.left)
        
        r_is_valid, r_min_, r_max_ = True, root.val, root.val
        if root.right is not None:
            r_min_, r_max_, r_is_valid = self._f(root.right)

        if root.left is not None and root.right is not None:
            return l_min_, r_max_, l_is_valid and r_is_valid and l_max_ < root.val < r_min_
        elif root.left is not None:
            return l_min_, root.val, l_is_valid and l_max_ < root.val
        elif root.right is not None:
            return root.val, r_max_, r_is_valid and root.val < r_min_
        return root.val, root.val, True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._f(root)[2]


if __name__ == "__main__":
    sln = Solution()
    print(sln.isValidBST(TreeNode.from_list([0, -1])))
    print(sln.isValidBST(TreeNode.from_list([2,1,3])))
    print(sln.isValidBST(TreeNode.from_list([2,2,2])))
    print(sln.isValidBST(TreeNode.from_list([5,1,4,None,None,3,6])))