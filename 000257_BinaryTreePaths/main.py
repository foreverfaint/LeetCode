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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]
        
        ans = []
        if root.left is not None:
            for p in self.binaryTreePaths(root.left):
                ans.append(f"{root.val}->{p}")
        
        if root.right is not None:
            for p in self.binaryTreePaths(root.right):
                ans.append(f"{root.val}->{p}")
        
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.binaryTreePaths(TreeNode.from_list([1,2,3,None,5])))
    print(sln.binaryTreePaths(TreeNode.from_list([1])))