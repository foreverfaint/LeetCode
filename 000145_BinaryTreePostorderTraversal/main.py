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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []

        if root:
            if root.left:
                r += self.postorderTraversal(root.left)
            if root.right:
                r += self.postorderTraversal(root.right)
            r.append(root.val)
        
        return r


if __name__ == "__main__":
    sln = Solution()
    print(TreeNode.from_list([1, None, 2, 3]))
    print(sln.postorderTraversal(TreeNode.from_list([1, None, 2, 3])))
    print(sln.postorderTraversal(TreeNode.from_list([])))
    print(sln.postorderTraversal(TreeNode.from_list([1])))