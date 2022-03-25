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
        ans = []
        from queue import Queue
        q = Queue()
        q.put_nowait(self)
        while not q.empty():
            first = q.get_nowait()
            if not first:
                ans.append(None)    
                continue

            ans.append(first.val)
            q.put_nowait(first.left)
            q.put_nowait(first.right)

        return ans

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

            if i < l and lst[i] is not None:
                r.left = cls(lst[i])
                q.put_nowait(r.left)

            i += 1
            if i < l and lst[i] is not None:
                r.right = cls(lst[i])
                q.put_nowait(r.right)

            i += 1

        return root


class Solution:
    def foo(self, root):
        if root.left is None and root.right is None:
            return 1, 1
        elif root.left is None:
            r_leaf, r_inner = self.foo(root.right)
            return 1 + r_leaf, max(1 + r_leaf, r_inner)
        elif root.right is None:
            l_leaf, l_inner = self.foo(root.left)
            return 1 + l_leaf, max(1 + l_leaf, l_inner)
        else:
            r_leaf, r_inner = self.foo(root.right)
            l_leaf, l_inner = self.foo(root.left)
            return max(r_leaf, l_leaf) + 1, max([r_leaf + l_leaf + 1, r_inner, l_inner])

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, dia = self.foo(root)
        return dia - 1


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([1,2,3,4,5])
    print(sln.diameterOfBinaryTree(tree))

    tree = TreeNode.from_list([1,2])
    print(sln.diameterOfBinaryTree(tree))