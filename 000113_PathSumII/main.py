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
    def foo(self, root, targetSum, path, pathColl):
        print("root.val=", root.val, "targetSum=", targetSum, "path=", path, "PathColl=", pathColl)
        if not root:
            return path

        if root.val == targetSum and root.left is None and root.right is None:
            new_path = list(path)
            new_path.append(root.val)
            pathColl.append(new_path)
            return path

        path.append(root.val)
        if root.left:
            path = self.foo(root.left, targetSum - root.val, path, pathColl)
        if root.right:
            path = self.foo(root.right, targetSum - root.val, path, pathColl)
        return path[:-1]
        

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        pathColl = []
        self.foo(root, targetSum, [], pathColl)
        return pathColl


if __name__ == "__main__":
    sln = Solution()


    root = TreeNode.from_list([-2,None,-3])
    print(sln.pathSum(root, -5))

    # root = TreeNode.from_list([5,4,8,11,None,13,4,7,2,None,None,5,1])
    # print(sln.pathSum(root, 22))

    # root = TreeNode.from_list([1,2,3])
    # print(sln.pathSum(root, 5))

    # root = TreeNode.from_list([1,2])
    # print(sln.pathSum(root, 0))