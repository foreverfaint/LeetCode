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
    def trimBST(
        self, node: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if node.left is None and node.right is None:
            return node if low <= node.val <= high else None
        
        new_left = None
        if node.left is not None and node.val > low:
            new_left = self.trimBST(node.left, low, high)
        
        new_right = None
        if node.right is not None and node.val < high:
            new_right = self.trimBST(node.right, low, high)

        if low <= node.val <= high:
            node.left = new_left
            node.right = new_right
            return node
        elif low > node.val:
            return new_right
        elif high < node.val:
            return new_left


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([1, 0, 2])
    print(sln.trimBST(tree, 1, 2).to_list())

    tree = TreeNode.from_list([3, 0, 4, None, 2, None, None, 1])
    print(sln.trimBST(tree, 1, 3).to_list())
