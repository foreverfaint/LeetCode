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
    def foo(self, root, ans):
        if root.left is None and root.right is None:
            ans.append(0)
            return root.val
        elif root.left is None:
            val = self.foo(root.right, ans)
            ans.append(abs(0 - val))
            return val + root.val
        elif root.right is None:
            val = self.foo(root.left, ans)
            ans.append(abs(0 - val))
            return val + root.val
        else:
            val_l = self.foo(root.left, ans)
            val_r = self.foo(root.right, ans)
            ans.append(abs(val_l - val_r))
            return val_l + val_r + root.val

    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = []
        self.foo(root, ans)
        return sum(ans)


if __name__ == "__main__":
    sln = Solution()
    print(sln.findTilt(TreeNode.from_list([1,2,3])))
    print(sln.findTilt(TreeNode.from_list([4,2,9,3,5,None,7])))
    print(sln.findTilt(TreeNode.from_list([21,7,14,1,1,2,2,3,3])))