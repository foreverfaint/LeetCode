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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if root.val > val:
            if root.left is not None:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right is not None:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        return root



if __name__ == "__main__":
    sln = Solution()
    print(sln.insertIntoBST(TreeNode.from_list([4,2,7,1,3]), 5))
    print(sln.insertIntoBST(TreeNode.from_list([40,20,60,10,30,50,70]), 25))
    print(sln.insertIntoBST(TreeNode.from_list([4,2,7,1,3,None,None,None,None,None,None]), 5))