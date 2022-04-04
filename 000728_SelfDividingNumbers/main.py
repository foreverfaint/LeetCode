from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for n in range(left, right + 1):
            if all([d != 0 and n % d == 0 for d in [int(c) for c in str(n)]]):
                ans.append(n)
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.selfDividingNumbers(1, 22))
    print(sln.selfDividingNumbers(47, 85))