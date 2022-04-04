from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return len([n1 for n1 in arr1 if all([abs(n1 - n2) > d for n2 in arr2])])


if __name__ == "__main__":
    sln = Solution()
    print(sln.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
    print(sln.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))
    print(sln.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))