from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return self.__str__()

    def as_list(self):
        return [self.val] + (self.left.as_list() if self.left else [None]) + (self.right.as_list() if self.right else [None])

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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:   
        if not root2:
            return root1

        if not root1:
            return root2

        merged_root = TreeNode(root1.val + root2.val)
        merged_root.left = self.mergeTrees(root1.left, root2.left)
        merged_root.right = self.mergeTrees(root1.right, root2.right)
        return merged_root


if __name__ == "__main__":
    sln = Solution()
    print(sln.mergeTrees(TreeNode.from_list([1,3,2,5]), TreeNode.from_list([2,1,3,None,4,None,7])).as_list())
    # print(sln.mergeTrees(TreeNode.from_list([1]), TreeNode.from_list([1,2])).as_list())