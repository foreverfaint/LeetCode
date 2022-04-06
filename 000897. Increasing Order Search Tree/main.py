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
            return root, root
        elif root.left is None:
            r_head, r_tail = self.foo(root.right)
            root.right = r_head
            return root, r_tail
        elif root.right is None:
            l_head, l_tail = self.foo(root.left)
            root.left = None
            l_tail.right = root
            return l_head, root
        else:
            l_head, l_tail = self.foo(root.left)
            r_head, r_tail = self.foo(root.right)
            root.left = None
            root.right = None
            l_tail.right = root
            root.right = r_head
            return l_head, r_tail

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        head, _ = self.foo(root)
        return head


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([5,3,6,2,4,None,8,1,None,None,None,7,9])
    print(sln.increasingBST(tree).to_list())

    tree = TreeNode.from_list([5,1,7])
    print(sln.increasingBST(tree).to_list())