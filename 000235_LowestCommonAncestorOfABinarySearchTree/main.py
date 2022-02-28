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
    def _f(self, root, k):
        if root is None:
            return []
        
        if root.val == k:
            return [k]

        if root.left is not None:
            r = self._f(root.left, k)
            if r: 
                return [root.val] + r
        
        if root.right is not None:
            r = self._f(root.right, k)
            if r:
                return [root.val] + r

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_r = self._f(root, p.val)
        q_r = self._f(root, q.val)
        i = 0
        l = min(len(p_r), len(q_r))
        while i < l:
            if p_r[i] != q_r[i]:
                break
            i += 1
        return TreeNode(p_r[i - 1])


if __name__ == "__main__":
    sln = Solution()
    print(sln.lowestCommonAncestor(TreeNode.from_list([6,2,8,0,4,7,9,None,None,3,5]), TreeNode(2), TreeNode(8)))
    print(sln.lowestCommonAncestor(TreeNode.from_list([6,2,8,0,4,7,9,None,None,3,5]), TreeNode(2), TreeNode(4)))
    print(sln.lowestCommonAncestor(TreeNode.from_list([2,1]), TreeNode(2), TreeNode(1)))