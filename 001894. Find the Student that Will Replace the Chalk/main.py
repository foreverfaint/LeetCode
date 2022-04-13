from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        for i, ch in enumerate(chalk):
            if ch > k:
                return i
            k -= ch


if __name__ == "__main__":
    sln = Solution()
    print(sln.chalkReplacer(chalk = [5,1,5], k = 22))
    print(sln.chalkReplacer(chalk = [3,4,1,2], k = 25))