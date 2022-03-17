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
    def find(self, root, key):
        if not root:
            return None

        if root.val == key:
            return root
        elif root.val < key:
            return self.find(root.right, key)
        else:
            return self.find(root.left, key)

    def merge(self, this, other):
        curr = this
        while curr.right is not None:
            curr = curr.right
        curr.right = other
        return this

    def delete(self, root, target):
        if root is None:
            return root

        if root is target:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                return self.merge(root.left, root.right)
        
        if root.left is not None:
            root.left = self.delete(root.left, target)

        if root.right is not None:
            root.right = self.delete(root.right, target)

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        target = self.find(root, key)
        if not target:
            return root
        return self.delete(root, target)


if __name__ == "__main__":
    sln = Solution()

    root = TreeNode.from_list([5,3,6,2,4,None,7])
    print(sln.deleteNode(root, 3))

    root = TreeNode.from_list([5,3,6,2,4,None,7])
    print(sln.deleteNode(root, 0))

    root = TreeNode.from_list([])
    print(sln.deleteNode(root, 0))
    # print(sln.find(root, 3))

    # other = TreeNode.from_list([5,4,6])
    # this = TreeNode.from_list([2,1,3])
    # print(sln.merge(this, other))