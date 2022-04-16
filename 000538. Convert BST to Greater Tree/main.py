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
    def foo(self, root, acc):
        if root.left is None and root.right is None:
            root.val += acc
            return root.val
        elif root.left is None:
            root.val += self.foo(root.right, acc)
            return root.val
        elif root.right is None:
            root.val += acc
            return self.foo(root.left, root.val)
        else:
            root.val += self.foo(root.right, acc)
            return self.foo(root.left, root.val)


    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.foo(root, 0)
        return root


if __name__ == "__main__":
    sln = Solution()

    # tree = TreeNode.from_list([7,None,8])
    # print(sln.convertBST(tree).to_list())

    # tree = TreeNode.from_list([6,5, 7, None, None, None, 8])
    # print(sln.convertBST(tree).to_list())

    # tree = TreeNode.from_list([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
    # print(sln.convertBST(tree).to_list())

    # tree = TreeNode.from_list([0,None,1])
    # print(sln.convertBST(tree).to_list())

    tree = TreeNode.from_list([3,2,4,1])
    print(sln.convertBST(tree).to_list())
