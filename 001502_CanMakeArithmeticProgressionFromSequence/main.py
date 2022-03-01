from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        l = len(arr)
        if l <= 2:
            return True

        arr = sorted(arr)
        diff = arr[1] - arr[0]
        i = 2
        while i < l:
            if arr[i] - arr[i - 1] != diff:
                return False
            i += 1
        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.canMakeArithmeticProgression([3,5,1]))
    print(sln.canMakeArithmeticProgression([1,2,4]))