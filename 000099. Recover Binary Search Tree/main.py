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
    def traverse_inorder(self, root):
        if root.left is None and root.right is None:
            return [root]
        
        ans = []
        if root.left is not None:
            ans.extend(self.traverse_inorder(root.left))
        
        ans.append(root)

        if root.right is not None:
            ans.extend(self.traverse_inorder(root.right))

        return ans

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        actual = self.traverse_inorder(root)
        expected = sorted(actual, key=lambda n: n.val)
        for n1, n2 in zip(actual, expected):
            if n1.val != n2.val:
                n1.val, n2.val = n2.val, n1.val
                break
        


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([1,3,None,None,2])
    print(tree.to_list())
    sln.recoverTree(tree)
    print(tree.to_list())

    tree = TreeNode.from_list([3,1,4,None,None,2])
    print(tree.to_list())
    sln.recoverTree(tree)
    print(tree.to_list())