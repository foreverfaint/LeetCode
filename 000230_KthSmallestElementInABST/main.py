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
    def foo(self, root, k):
        if root is None:
            return []

        ans = []
        if root.left:
            ans.extend(self.foo(root.left, k))
        
        if len(ans) > k:
            return ans

        ans.append(root.val)
        
        if len(ans) > k:
            return ans

        
        if root.right:
            ans.extend(self.foo(root.right, k))

        return ans

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.foo(root, k)[k-1]


if __name__ == "__main__":
    sln = Solution()
    print(sln.kthSmallest(TreeNode.from_list([3,1,4,None,2]), 1))
    print(sln.kthSmallest(TreeNode.from_list([5,3,6,2,4,None,None,1]), 3))