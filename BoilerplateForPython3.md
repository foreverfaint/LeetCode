# Boilerplate for Python3

## Basic

```python
from typing import List


class Solution:
    pass


if __name__ == "__main__":
    sln = Solution()
```

## ListNode

```python
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list() -> List[int]:
        if self.next is None:
            return []
        return [self.val] + self.next.to_list()

    @classmethod
    def from_list(cls, lst: List[int]) -> "ListNode":
        if lst is None or len(lst) == 0:
            return None
        return ListNode(lst[0], cls.from_list(lst[1:]))


class Solution:
    pass


if __name__ == "__main__":
    sln = Solution()
```

## TreeNode

```python
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
    pass


if __name__ == "__main__":
    sln = Solution()
```