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


class BSTIterator:
    def foo(self, root, q):
        if not root:
            return
        if root.left:
            self.foo(root.left, q)
        q.put_nowait(root.val)
        if root.right:
            self.foo(root.right, q)

    def __init__(self, root: Optional[TreeNode]):
        from queue import Queue
        self.q = Queue()
        self.foo(root, self.q)

    def next(self) -> int:
        return self.q.get_nowait()
        
    def hasNext(self) -> bool:
        return not self.q.empty()


if __name__ == "__main__":
    it = BSTIterator(TreeNode.from_list([7, 3, 15, None, None, 9, 20]))
    print(it.next())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())            
        