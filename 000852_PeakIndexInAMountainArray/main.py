from selectors import EpollSelector
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return i - 1
        return -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.peakIndexInMountainArray([0,1,0]))
    print(sln.peakIndexInMountainArray([0,2,1,0]))
    print(sln.peakIndexInMountainArray([0,10,5,2]))