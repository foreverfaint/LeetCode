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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        m = {}

        from collections import deque
        q = deque()
        q.append((root, 0))

        while len(q) > 0:
            node, lvl = q.popleft()
            m.setdefault(lvl, [])
            m[lvl].append(node.val)

            if node.left is not None:
                q.append((node.left, lvl + 1))
            if node.right is not None:
                q.append((node.right, lvl + 1))

        m = sorted(m.items(), key=lambda kv: kv[0])
        return [sum(arr) / len(arr) for _, arr in m]


if __name__ == "__main__":
    sln = Solution()

    root = TreeNode.from_list([3,9,20,None,None,15,7])
    print(sln.averageOfLevels(root))

    root = TreeNode.from_list([3,9,20,15,7])
    print(sln.averageOfLevels(root))