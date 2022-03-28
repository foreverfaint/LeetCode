from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1

        m = {0: 1}
        for i in range(1, target + 1):
            s = 0
            for n in [n for n in nums if n <= i]:
                s += m[i - n]
            m[i] = s

        return m[target]


if __name__ == "__main__":
    sln = Solution()
    print(sln.combinationSum4([1,2,3], 4))
    print(sln.combinationSum4([9], 3))