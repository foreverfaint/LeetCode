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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None

        assert len(preorder) == len(inorder)

        val = preorder[0]

        i = 0
        while inorder[i] != val and i < len(inorder):
            i += 1

        left_preorder = preorder[1:1+i]
        left_inorder = inorder[0:i]
        right_preorder = preorder[1+i:]
        right_inorder = inorder[i+1:]
        return TreeNode(val, left=self.buildTree(left_preorder, left_inorder), right=self.buildTree(right_preorder, right_inorder))


if __name__ == "__main__":
    sln = Solution()

    print(sln.buildTree([3,9,20,15,7], [9,3,15,20,7]))
    print(sln.buildTree([-1], [-1]))
    print(sln.buildTree([3,9,10], [3,9,10]))
    print(sln.buildTree([3,9,10], [10,9,3]))