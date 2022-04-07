from typing import List


class NestedInteger:
    def __init__(self, x_or_lst) -> None:
        if isinstance(x_or_lst, int):
            self.x = x_or_lst
            self.lst = None
        else:
            self.x = None
            self.lst = x_or_lst

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self.x is not None

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.x

    def getList(self) -> List["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.lst

    def to_list(self):
        if self.x:
            return self.x
        return [x.to_list() for x in self.lst]

    @classmethod
    def from_list(cls, data):
        if isinstance(data, int):
            return cls(data)
        return cls([cls.from_list(x) for x in data])


def flatten(nestedList: List[NestedInteger]):
    ans = []
    for ni in nestedList:
        if ni.isInteger():
            ans.append(ni.getInteger())
        else:
            for nj in flatten(ni.getList()):
                ans.append(nj)
    return ans


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.data = flatten(nestedList)
    
    def next(self) -> int:
        res = self.data[0]
        self.data = self.data[1:]
        return res
    
    def hasNext(self) -> bool:
        return len(self.data) > 0


if __name__ == "__main__":
    ni = NestedInteger.from_list([[1,1],2,[1,1]])
    it = NestedIterator([ni])
    ans = []
    while it.hasNext():
        ans.append(it.next())
    print(ans)

    ni = NestedInteger.from_list([1,[4,[6]]])
    it = NestedIterator([ni])
    ans = []
    while it.hasNext():
        ans.append(it.next())
    print(ans)