from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self) -> List[int]:
        if self.next is None:
            return [self.val]
        return [self.val] + self.next.to_list()

    @classmethod
    def from_list(cls, lst: List[int]) -> "ListNode":
        if lst is None or len(lst) == 0:
            return None
        return ListNode(lst[0], cls.from_list(lst[1:]))


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
    def dfs(self, head, root):
        if not head:
            return True
        if not root:
            return False
        return root.val == head.val and (self.dfs(head.next, root.left) or self.dfs(head.next, root.right))

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


if __name__ == "__main__":
    sln = Solution()

    head = ListNode.from_list([1,10,3,7,10,8,9,5,3,9,6,8,7,6,6,3,5,4,4,9,6,7,9,6,9,4,9,9,7,1,5,5,10,4,4,10,7,7,2,4,5,5,2,7,5,8,6,10,2,10,1,1,6,1,8,4,7,10,9,7,9,9,7,7,7,1,5,9,8,10,5,1,7,6,1,2,10,5,7,7,2,4,10,1,7,10,9,1,9,10,4,4,1,2,1,1,3,2,6,9])
    root = TreeNode.from_list([4,None,8,None,5,None,7,None,5,None,2,1,3,None,None,None,6,8,9,None,None,None,3,None,2,None,10,None,7,None,8,3,4,None,None,None,3,5,1,None,None,None,3,1,7,None,None,None,4,7,7,None,None,8,3,None,None,None,6,3,1,None,None,None,1,None,8,None,2,5,5,None,None,1,3,None,None,None,5,None,3,3,5,None,None,None,7,None,10,None,7,None,6,None,8,None,4,None,10,None,6,None,6,9,3,None,None,6,5,None,None,None,5,None,2,None,7,None,5,None,4,8,2,None,None,None,2,None,10,10,8,None,None,None,7,None,2,None,5,8,6,None,None,None,5,None,7,None,3,4,5,None,None,None,4,None,8,None,8,None,8,None,2,None,5,2,9,None,None,None,2,None,3,7,1,None,None,10,1,None,None,None,7,None,6,None,6,None,7,None,7,None,4,4,2,None,None,7,4,None,None,None,7,None,3,7,5,None,None,None,5,None,4,None,9,5,2,None,None,None,4,None,9,None,5,None,5,None,5,None,2,None,5,None,2,None,5,None,7,5,5,None,None,None,6,None,1,None,7,None,3,9,8,None,None,None,4,None,7,4,8,None,None,4,2,None,None,None,3,10,2,None,None,None,7,None,10,None,3,None,1,None,2,None,5,None,9,None,8,None,5,None,9,None,3,None,7,None,10,5,2,None,None,None,2,8,10,None,None,None,4,4,7,None,None,None,5,1,4,None,None,None,10,None,9,None,4,None,9,6,5,None,None,None,7,5,4,None,None,None,8,None,8,4,9,None,None,None,6,9,1,None,None,None,3,3,6,None,None,None,6,None,7,None,2,None,1,None,8,2,9,None,None,None,8,None,3,None,1,9,1,None,None,None,2,None,6,None,1,None,6,3,9,None,None,None,10,None,1,None,9,None,9,None,10,None,2,None,6,None,3,None,7,None,2,None,2,None,2,9,5,None,None,None,5,None,6,None,6,None,2,None,5,7,9,None,None,None,6,10,4,None,None,8,4,None,None,4,2,None,None,4,7,None,None,2,5,None,None,None,4,5,1,None,None,None,3,None,1,10,6,None,None,3,2,None,None,None,6,None,9,None,7,None,5,8,5,None,None,None,5,None,5,10,6,None,None,None,7,None,1,None,6,3,7,None,None,None,9,7,1,None,None,None,7,None,4,None,4,None,9,None,4,None,1,None,10,None,1,10,10,None,None,None,6,None,3,None,1,None,9,None,7,None,6,6,1,None,None,None,9,4,7,None,None,None,3,None,10,None,4,3,3,None,None,None,4,5,10,None,None,None,1,8,10,None,None,None,6,None,9,None,10,None,4,4,9,None,None,None,3,None,3,None,3,None,10,None,10,None,6,8,1,None,None,None,9,7,1,None,None,None,5,None,3,None,10,None,5,None,9,None,5,None,8,None,6,3,2,None,None,None,8,None,8,3,9,None,None,None,9,None,10,3,8,None,None,6,6,None,None,None,6,None,8,None,2,None,9,None,4,None,6,None,4,None,4,None,6,None,9,None,7,None,10,None,1,None,3,None,6,None,7,None,4,None,9,None,1,None,3,8,10,None,None,None,2,None,10,None,4,None,8,None,10,None,7,None,8,5,1,None,None,9,3,None,None,7,8,None,None,None,1,None,1,5,4,None,None,None,1,None,4,5,7,None,None,None,3,None,6,None,6,None,9,None,4,None,1,5,10,None,None,None,3,None,7,None,10,None,8,None,9,2,5,None,None,None,3,None,9,10,6,None,None,None,8,None,7,8,6,None,None,None,6,None,3,None,5,None,4,None,4,None,9,None,6,2,7,None,None,None,9,None,6,1,9,None,None,None,4,None,9,9,9,None,None,None,7,7,1,None,None,None,5,None,5,6,10,None,None,None,4,None,4,10,10,None,None,None,7,2,7,None,None,None,2,None,4,None,5,None,5,10,2,None,None,None,7,9,5,None,None,None,8,None,6,None,10,8,2,None,None,8,10,None,None,None,1,None,1,None,6,5,1,None,None,8,8,None,None,8,4,None,None,None,7,None,10,4,9,None,None,None,7,None,9,None,9,1,7,None,None,4,7,None,None,None,7,None,1,None,5,8,9,None,None,9,8,None,None,9,10,None,None,4,5,None,None,1,1,None,None,None,7,None,6,None,1,None,2,1,10,None,None,2,5,None,None,7,7,None,None,None,7,None,2,None,4,3,10,None,None,None,1,None,7,None,10,7,9,None,None,None,5,4,9,None,None,None,10,6,4,None,None,8,4,None,None,None,1,None,2,None,1,8,1,None,None,None,3,None,2,None,6,None,9,None,2,1,10,None,None,None,5,None,8,2,1,None,None,None,2,3,10,None,None,None,8,None,9,None,5,None,4,None,1,9,10,None,None,4,9,None,None,3,5,None,None,None,6,None,6,9,1,None,None,None,5,None,2,None,2,None,6,None,1,7,9,None,None,None,6,None,8,4,4,None,None,None,2,None,10,None,1,None,2,None,9,None,8,None,2,None,1,10,4,None,None,None,10,None,8,3,2,None,None,None,10,None,3,8,1,None,None,5,3,None,None,None,6,None,8,None,7,2,5,None,None,1,6,None,None,None,8,None,6,None,3,None,8,None,9,None,5,None,2,None,9,None,2,6,10,None,None,7,10,None,None,None,6,None,8,None,7,7,4,None,None,None,3,5,2,None,None,10,4,None,None,None,4,4,3,None,None,None,5,None,1,None,10,None,10,None,5,None,9,None,3,None,8,None,3,None,2,None,4,1,1,None,None,None,7,10,8,None,None,None,9,4,8,None,None,1,2,None,None,9,7,None,None,5,8,None,None,None,9,None,7,None,4,None,4,5,3,None,None,None,2,None,4,3,10,None,None,7,7,None,None,None,2,None,2,8,8,None,None,None,2,None,4,None,5,8,4,None,None,None,9,None,4,None,10,None,4,None,5,None,5,None,1,None,5,None,8,None,5,None,5,None,1,None,10,None,9,None,10,None,2,None,7,5,9,None,None,None,6,4,6,None,None,None,2,None,10,None,1,4,3,None,None,7,8,None,None,None,3,None,3,None,8,None,10,None,6,6,10,None,None,None,1,8,5,None,None,1,3,None,None,None,8,None,9,None,10,None,8,4,9,None,None,10,1,None,None,None,2,None,8,5,2,None,None,8,6,None,None,None,4,None,7,10,1,None,None,None,3,3,3,None,None,None,3,None,5,7,3,None,None,10,9,None,None,None,2,None,8,None,10,None,7,None,10,None,3,9,10,None,None,None,6,4,9,None,None,9,3,None,None,None,7,None,2,None,10,None,10,None,7,None,4,5,7,None,None,9,8,None,None,None,6,3,1,None,None,None,9,None,7,4,4,None,None,None,6,None,1,None,9,None,9,None,3,1,1,None,None,1,8,None,None,None,1,None,2,None,7,4,6,None,None,None,1,None,3,None,8,None,10,None,3,None,10,None,10,None,10,None,10,None,10,None,6,None,7,None,3,None,9,None,7,5,4,None,None,None,5,None,5,1,3,None,None,None,6,3,4,None,None,None,3,2,10,None,None,10,5,None,None,None,5,9,1,None,None,None,8,None,7,None,9,5,3,None,None,None,2,None,7,None,10,None,2,9,4,None,None,None,4,10,10,None,None,None,6,2,6,None,None,None,4,None,5,None,7,None,7,None,2,4,1,None,None,None,7,None,5,8,8,None,None,3,6,None,None,None,1,None,5,None,8,4,6,None,None,None,6,None,9,None,4,None,4,None,3,None,2,6,9,None,None,None,6,6,8,None,None,None,7,None,5,None,5,None,9,4,3,None,None,None,10,4,6,None,None,None,9,None,3,None,10,None,9,None,1,None,6,None,1,None,4,None,5,5,3,None,None,7,8,None,None,None,6,None,6,None,5,9,4,None,None,None,9,None,7,None,7,7,5,None,None,None,7,None,3,8,3,None,None,None,1,5,4,None,None,None,2,None,3,None,4,None,5,5,6,None,None,None,2,None,2,7,9,None,None,9,5,None,None,None,9,None,9,None,8,7,6,None,None,None,2,None,9,None,2,None,7,6,4,None,None,None,1,None,7,None,2,None,7,None,3,9,2,None,None,4,5,None,None,None,3,None,2,None,8,7,8,None,None,7,7,None,None,None,10,None,9,2,7,None,None,6,3,None,None,None,10,None,5,None,7,None,9,None,3,None,1,None,9,None,2,5,2,None,None,None,4,None,8,None,6,10,10,None,None,10,3,None,None,None,3,None,1,None,3,None,8,3,2,None,None,None,5,2,8,None,None,7,5,None,None,7,7,None,None,None,1,6,5,None,None,None,2,None,4,None,7,None,5,None,3,None,7,None,10,None,10,None,7,None,9,None,5,5,5,None,None,None,9,None,4,None,7,None,6,None,2,None,3,None,3,8,10,None,None,None,1,None,3,None,6,None,10,None,8,None,6,4,5,None,None,None,6,None,3,None,3,None,8,1,3,None,None,2,3,None,None,None,7,None,10,None,2,None,10,None,2,None,7,None,10,6,7,None,None,3,4,None,None,6,2,None,None,None,9,None,8,None,7,None,10,None,9,10,1,None,None,None,5,1,10,None,None,10,2,None,None,None,2,5,8,None,None,None,9,8,8,None,None,None,8,None,4,1,3,None,None,None,4,None,4,None,9,None,4,10,7,None,None,10,4,None,None,4,5,None,None,9,2,None,None,3,7,None,None,8,7,None,None,None,5,None,10,None,3,None,8,None,3,None,5,2,9,None,None,None,10,None,3,None,10,None,7,5,1,None,None,2,4,None,None,None,5,None,2,None,6,None,8,None,9,None,10,None,9,None,6,None,2,6,7,None,None,2,7,None,None,None,3,None,6,9,5,None,None,2,6,None,None,None,8,None,4,None,8,None,2,4,9,None,None,4,7,None,None,None,9,None,5,None,3,None,8,None,6,None,5,7,4,None,None,8,7,None,None,None,9,1,2,None,None,None,9,6,7,None,None,None,8,None,6,None,6,4,6,None,None,None,3,None,5,10,4,None,None,None,5,None,8,None,8,None,7,None,10,5,10,None,None,None,10,None,10,None,10,8,2,None,None,5,3,None,None,None,8,6,6,None,None,10,8,None,None,1,8,None,None,None,9,1,6,None,None,7,6,None,None,None,10,5,4,None,None,None,10,5,4,None,None,2,5,None,None,None,4,2,5,None,None,None,3,None,4,2,8,None,None,None,5,None,9,None,3,9,3,None,None,None,5,None,7,None,7,None,5,None,10,None,3,2,7,None,None,3,8,None,None,None,10,2,3,None,None,None,7,3,3,None,None,None,6,None,4,None,8,None,3,None,3,None,1,None,9,10,1,None,None,None,1,None,6,6,5,None,None,6,3,None,None,None,6,None,4,None,2,None,10,None,9,2,5,None,None,None,10,None,10,3,5,None,None,10,6,None,None,1,9,None,None,6,7,None,None,6,5,None,None,None,8,None,8,5,6,None,None,None,6,None,8,None,8,None,4,None,6,None,9,None,2,None,1,None,10,None,9,None,9,None,4,1,6,None,None,None,1,None,3,None,4,10,8,None,None,None,7,None,5,None,10,None,1,None,9,None,9,None,9,1,8,None,None,None,1,None,9,5,1,None,None,7,1,None,None,None,8,None,1,8,6,None,None,2,9,None,None,10,5,None,None,None,2,None,10,None,10,None,9,None,10,None,7,None,7,None,5,None,8,8,2,None,None,None,9,None,10,None,1,None,1,None,1,None,10,6,1,None,None,None,9,None,2,9,9,None,None,None,9,3,8,None,None,None,1,None,10,1,10,None,None,None,8,None,7,None,8,None,8,6,5,None,None,2,5,None,None,None,7,None,1,None,10,None,4,8,5,None,None,5,2,None,None,2,3,None,None,None,6,3,10,None,None,1,8,None,None,None,9,None,8,7,10,None,None,None,10,None,5,10,6,None,None,None,5,None,6,None,5,6,6,None,None,5,8,None,None,None,7,None,8,None,10,1,1,None,None,None,10,1,2,None,None,9,5,None,None,None,7,4,5,None,None,None,10,None,3,None,5,None,8,None,2,None,9,None,9,6,7,None,None,7,1,None,None,None,5,None,2,None,8,5,3,None,None,None,7,None,6,None,6,None,7,None,5,None,1,6,7,None,None,None,6,None,8,None,8,None,5,10,10,None,None,None,10,5,2,None,None,6,5,None,None,8,1,None,None,2,3,None,None,9,3,None,None,10,7,None,None,1,4,None,None,5,10,None,None,None,7,None,6,None,1,None,9,None,8,None,2,10,7,None,None,None,5,3,9,None,None,None,2,None,7,None,3,None,7,None,7,9,2,None,None,None,5,None,6,1,2,None,None,5,10,None,None,6,9,None,None,None,10,9,8,None,None,5,9,None,None,None,10,5,6,None,None,None,10,10,1,None,None,None,7,None,10,None,3,None,2,None,6,9,9,None,None,2,5,None,None,None,1,None,8,None,2,None,4,2,9,None,None,None,10,None,6,None,5,2,3,None,None,None,1,None,7,None,10,6,10,None,None,None,2,5,9,None,None,4,7,None,None,None,2,1,1,None,None,None,9,None,5,7,7,None,None,None,3,None,4,None,10,2,6,None,None,8,6,None,None,1,10,None,None,None,10,4,4,None,None,None,7,None,8,7,5,None,None,None,2,10,6,None,None,3,6,None,None,None,10,None,8,None,8,8,9,None,None,None,7,None,8,None,1,None,5,None,8,None,7,10,6,None,None,None,3,None,5,None,6,9,10,None,None,None,10,None,6,None,2,None,2,None,2,None,9,None,7,None,4,5,9,None,None,None,4,None,4,None,3,None,10,None,3,10,3,None,None,5,7,None,None,None,6,None,3,3,4,None,None,None,7,None,6,None,10,None,5,8,8,None,None,None,4,5,5,None,None,None,2,None,10,None,2,None,1,2,8,None,None,None,5,None,8,None,3,None,4,None,8,None,1,None,5,8,1,None,None,3,9,None,None,None,3,1,1,None,None,5,9,None,None,None,6,None,9,5,6,None,None,None,5,3,5,None,None,None,9,3,1,None,None,3,5,None,None,3,10,None,None,None,10,None,8,None,1,None,7,None,4,None,1,None,7,None,1,None,3,7,9,None,None,1,2,None,None,None,8,3,7,None,None,None,8,None,1,6,6,None,None,None,9,7,4,None,None,6,10,None,None,4,5,None,None,None,1,None,7,None,6,7,3,None,None,None,6,None,9,None,8,2,6,None,None,6,8,None,None,2,7,None,None,None,8,None,8,7,5,None,None,None,4,None,9,5,3,None,None,9,5,None,None,None,5,None,1,None,5,None,6,8,6,None,None,None,5,None,4,None,2,8,5,None,None,None,9,None,5,None,9,None,3,None,5,9,3,None,None,None,2,None,7,None,8,None,8,None,8,None,10,7,2,None,None,None,6,None,2,1,10,None,None,None,6,None,8,None,4,None,6,8,5,None,None,None,3,None,1,None,6,None,6,None,2,None,9,1,9,None,None,None,3,None,7,4,7,None,None,9,6,None,None,7,8,None,None,None,1,5,1,None,None,7,10,None,None,None,6,None,8,3,2,None,None,1,5,None,None,None,8,None,3,None,3,9,1,None,None,None,8,None,1,3,5,None,None,None,9,None,8,3,4,None,None,None,9,None,1,None,3,None,7,None,3,5,1,None,None,None,4,None,1,None,5,None,1,None,3,4,8,None,None,None,1,10,7,None,None,None,1,None,9,None,7,None,3,None,10,6,9,None,None,None,3,6,8,None,None,None,8,None,3,None,4,None,10,None,2,10,7,None,None,5,4,None,None,None,4,2,6,None,None,1,10,None,None,None,4,3,7,None,None,None,4,None,1,None,6,None,10,None,7,4,9,None,None,None,10,9,4,None,None,None,6,5,9,None,None,None,7,1,7,None,None,None,4,None,4,None,4,None,6,4,3,None,None,None,4,None,5,None,10,None,2,None,1,None,1,None,2,None,2,9,4,None,None,None,9,None,9,9,4,None,None,None,5,None,6,None,2,None,3,None,10,9,10,None,None,10,2,None,None,3,9,None,None,None,9,None,10,None,9,None,3,None,1,5,6,None,None,None,6,None,2,None,9,None,3,None,9,9,3,None,None,5,3,None,None,None,2,None,3,None,8,None,2,None,9,None,3,None,4,None,3,None,4,None,8,6,7,None,None,None,6,None,3,None,1,None,9,5,1,None,None,None,2,None,7,4,7,None,None,None,2,None,9,None,7,None,10,None,6,None,7,None,1,None,4,None,5,None,2,None,7,None,3,None,7,None,4,None,5,None,10,None,1,None,9,9,8,None,None,10,10,None,None,None,6,6,10,None,None,10,4,None,None,4,6,None,None,None,4,None,3,None,5,4,8,None,None,None,5,6,3,None,None,1,7,None,None,9,4,None,None,None,9,10,2,None,None,None,5,None,6,2,5,None,None,None,10,5,1,None,None,None,8,2,2,None,None,7,6,None,None,None,9,None,4,None,4,None,2,None,4,None,8,1,10,None,None,None,8,None,3,None,1,None,5,None,2,None,9,8,5,None,None,8,6,None,None,None,1,None,6,None,2,2,9,None,None,None,9,5,7,None,None,None,4,None,5,4,5,None,None,1,1,None,None,8,3,None,None,None,10,7,10,None,None,6,5,None,None,6,3,None,None,4,1,None,None,10,1,None,None,4,2,None,None,6,3,None,None,None,2,None,9,None,10,9,9,None,None,None,2,None,8,None,8,6,2,None,None,10,7,None,None,None,10,1,3,None,None,2,3,None,None,None,10,3,1,None,None,None,9,None,4,None,3,None,4,None,7,None,2,None,1,None,9,None,1,None,7,None,9,None,7,None,6,7,9,None,None,None,10,None,6,3,2,None,None,None,4,None,4,None,5,4,1,None,None,None,3,None,3,None,6,None,5,None,4,10,5,None,None,4,6,None,None,10,4,None,None,None,7,None,10,None,1,None,1,5,6,None,None,9,7,None,None,None,3,None,6,None,8,None,2,None,4,None,2,None,7,None,8,3,10,None,None,None,6,None,3,None,7,None,4,2,3,None,None,1,9,None,None,5,6,None,None,6,6,None,None,None,7,None,8,9,9,None,None,None,9,None,1,None,9,None,5,None,1,None,5,2,6,None,None,None,9,2,4,None,None,3,6,None,None,4,2,None,None,None,9,None,6,3,3,None,None,None,7,None,9,None,6,2,9,None,None,None,8,None,5,None,4,None,7,None,4,None,8,None,5,3,2,None,None,None,1,None,1,None,1,None,1,None,1,None,1,None,4,None,6,3,7,None,None,9,7,None,None,9,2,None,None,None,4,None,1,None,5,None,8,None,2,10,1,None,None,None,10,None,1,2,7,None,None,None,5,None,8,None,7,2,6,None,None,None,10,None,3,None,7,None,3,None,6,9,4,None,None,None,2,None,8,None,8,None,1,None,8,None,8,None,9,None,7,None,5,10,9,None,None,4,4,None,None,None,7,None,6,None,8,1,3,None,None,9,3,None,None,1,10,None,None,None,9,8,2,None,None,None,8,None,4,None,4,4,1,None,None,None,7,None,8,1,9,None,None,None,10,None,3,6,7,None,None,None,5,5,2,None,None,None,4,None,5,6,6,None,None,7,7,None,None,5,10,None,None,None,6,10,6,None,None,None,2,None,5,2,5,None,None,None,7,None,7,None,7,None,4,None,9,None,4,None,8,None,1,None,5,None,9,6,4,None,None,None,8,9,2,None,None,10,2,None,None,None,3,None,4,None,10,None,6,None,10,2,9,None,None,6,1,None,None,None,7,6,6,None,None,None,2,None,4,None,10,8,9,None,None,None,7,3,9,None,None,10,4,None,None,None,10,None,6,None,2,None,5,None,1,None,8,8,3,None,None,None,2,5,10,None,None,5,8,None,None,3,10,None,None,None,5,None,8,None,5,None,4,None,5,6,2,None,None,None,7,None,5,None,10,None,8,1,5,None,None,None,1,None,1,None,5,None,9,None,6,None,1,None,5])
    print(sln.isSubPath(head, root))

    head = ListNode.from_list([3])
    root = TreeNode.from_list([1,5,3,None,4,None,3])
    print(sln.isSubPath(head, root))

    head = ListNode.from_list([4,2,8])
    root = TreeNode.from_list([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
    print(sln.isSubPath(head, root))

    head = ListNode.from_list([1,4,2,6])
    root = TreeNode.from_list([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
    print(sln.isSubPath(head, root))

    head = ListNode.from_list([1,4,2,6,8])
    root = TreeNode.from_list([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
    print(sln.isSubPath(head, root))

    head = ListNode.from_list([1,10])
    root = TreeNode.from_list([1,None,1,10,1,9])
    print(sln.isSubPath(head, root))

    head = ListNode.from_list([4,2,8])
    root = TreeNode.from_list([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
    print(sln.isSubPath(head, root))

    


    

