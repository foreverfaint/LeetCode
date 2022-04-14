from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = arr[-1]
        i = len(arr) - 2
        arr[-1] = -1
        while i >= 0:
            t = arr[i]
            arr[i] = max_
            max_ = max(t, max_)
            i -= 1
        return arr


if __name__ == "__main__":
    sln = Solution()
    print(sln.replaceElements([17,18,5,4,6,1]))
    print(sln.replaceElements([400]))