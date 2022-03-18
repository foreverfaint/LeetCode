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
    def foo(self, root, target):
        if root.val == target:
            return [root]

        if root.left:
            arr = self.foo(root.left, target)
            if arr:
                return [root] + arr
        
        if root.right:
            arr = self.foo(root.right, target)
            if arr:
                return [root] + arr
        
        return []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.foo(root, p.val)
        q_path = self.foo(root, q.val)
        p_i = 0
        q_i = 0
        while p_i < len(p_path) and q_i < len(q_path):
            if p_path[p_i] != q_path[q_i]:
                break
            p_i += 1
            q_i += 1
        return p_path[p_i - 1]


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([3,5,1,6,2,0,8,None,None,7,4])
    node = sln.lowestCommonAncestor(tree, TreeNode(5), TreeNode(1))
    print(node)

    tree = TreeNode.from_list([3,5,1,6,2,0,8,None,None,7,4])
    node = sln.lowestCommonAncestor(tree, TreeNode(5), TreeNode(4))
    print(node)

    tree = TreeNode.from_list([1,2])
    node = sln.lowestCommonAncestor(tree, TreeNode(1), TreeNode(2))        
    print(node)