from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def as_list(self):
        lst = []
        n = self
        while n: 
            n_2 = n
            while n_2:
                lst.append(n_2.val)
                n_2 = n_2.next
            lst.append("#")
            n = n.left
        return lst

    def __str__(self) -> str:
        return str(self.val) + "/" + str(self.next)

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_list(cls, lst: List[int]):
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            if root.left is not None:
                root.left.next = root.right
                self.connect(root.left)

            if root.right is not None:
                if root.next is not None:
                    root.right.next = root.next.left
                self.connect(root.right)

        return root


if __name__ == "__main__":
    sln = Solution()
    print(sln.connect(Node.from_list([1,2,3,4,5,6,7])).as_list())