from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for n in arr2:
            ans += [x for x in arr1 if x == n]
        ans += sorted([x for x in arr1 if x not in arr2])
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
    print(sln.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))