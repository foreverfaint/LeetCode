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
    def foo(self, root, m):
        if root:
            m.setdefault(root.val, 0)
            m[root.val] += 1
            self.foo(root.left, m)
            self.foo(root.right, m)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        m = {}
        self.foo(root, m)
        m = sorted(m.items(), key=lambda kv: kv[1], reverse=True)
        return [kv[0] for kv in m if kv[1] == m[0][1]]


if __name__ == "__main__":
    sln = Solution()

    tree = TreeNode.from_list([1,None,2,2])
    print(sln.findMode(tree))

    tree = TreeNode.from_list([0])
    print(sln.findMode(tree))