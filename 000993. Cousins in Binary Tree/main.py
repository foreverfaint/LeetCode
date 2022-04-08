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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        from collections import deque
        q = deque()
        q.append((root, 0, None))

        found_x = False
        found_y = False
        while len(q) > 0:
            current, lvl, parent = q.popleft()
            
            if current.left:
                q.append((current.left, lvl + 1, current))

            if current.right:
                q.append((current.right, lvl + 1, current))
            
            if current.val == x:
                found_x = (lvl, parent)
            elif current.val == y:
                found_y = (lvl, parent)

            if found_x and found_y and found_x[0] == found_y[0] and found_x[1] != found_y[1]:
                return True
        return False


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([1,2,3,4])
    print(sln.isCousins(tree, 4, 3))

    tree = TreeNode.from_list([1,2,3,None,4,None,5])
    print(sln.isCousins(tree, 5, 4))

    tree = TreeNode.from_list([1,2,3,None,4])
    print(sln.isCousins(tree, 2, 3))    