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
    def getHeight(self, root):
        if root is None:
            return 0, True
        elif root.left is not None and root.right is not None:
            h_left, is_balanced_left = self.getHeight(root.left)
            h_right, is_balanced_right = self.getHeight(root.right)
            return 1 + max(h_left, h_right), abs(h_left - h_right) <= 1 and is_balanced_left and is_balanced_right
        elif root.left is not None:
            h, _ = self.getHeight(root.left)
            return 1 + h, h <= 1
        elif root.right is not None:
            h, _ = self.getHeight(root.right)
            return 1 + h, h <= 1
        else:
            return 1, True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, is_balanced = self.getHeight(root)
        return is_balanced


if __name__ == "__main__":
    sln = Solution()
    print(sln.isBalanced(TreeNode.from_list([3,9,20,None,None,15,7])))
    print(sln.isBalanced(TreeNode.from_list([1,2,2,3,3,None,None,4,4])))
    print(sln.isBalanced(TreeNode.from_list([])))