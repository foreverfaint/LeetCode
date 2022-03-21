from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            x = i
            c = 0
            while x > 0:
                c += 1 if x % 2 == 1 else 0
                x = x >> 1
            ans.append(c) 
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.countBits(2))
    print(sln.countBits(5))