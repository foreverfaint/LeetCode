from typing import List


class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            ans += 1
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.numberOfSteps(14))
    print(sln.numberOfSteps(8))
    print(sln.numberOfSteps(123))