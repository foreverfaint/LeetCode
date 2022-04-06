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
    def leaf(self, root):
        if not root.left and not root.right:
            return [root.val]
        elif not root.left:
            return self.leaf(root.right)
        elif not root.right:
            return self.leaf(root.left)
        else:
            return self.leaf(root.left) + self.leaf(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = list(self.leaf(root1))
        leaf2 = list(self.leaf(root2))
        print(leaf1, leaf2)
        i = 0
        while i < len(leaf1) and i < len(leaf2):
            if leaf1[i] != leaf2[i]:
                return False
            i += 1
        return i == len(leaf1) and i == len(leaf2)


if __name__ == "__main__":
    sln = Solution()

    root1 = TreeNode.from_list([3,5,1,6,2,9,8,None,None,7,4])
    root2 = TreeNode.from_list([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
    print(sln.leafSimilar(root1, root2))

    root1 = TreeNode.from_list([1,2,3])
    root2 = TreeNode.from_list([1,3,2])
    print(sln.leafSimilar(root1, root2))    