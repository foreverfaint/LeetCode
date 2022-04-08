from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        inc = True
        for i in range(1, len(arr), 1):
            if inc:
                if arr[i] > arr[i - 1]:
                    continue
                elif arr[i] == arr[i - 1]:
                    return False
                if i == 1:
                    return False
                inc = False
            else:
                if arr[i] < arr[i - 1]:
                    continue
                return False
        return not inc


if __name__ == "__main__":
    sln = Solution()
    print(sln.validMountainArray([2,1]))
    print(sln.validMountainArray([3,5,5]))
    print(sln.validMountainArray([0,3,2,1]))
    print(sln.validMountainArray([0,1,2,3,4,5,6,7,8,9]))
    print(sln.validMountainArray([9,3,2,1]))