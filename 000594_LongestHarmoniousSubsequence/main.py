from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s = {}
        for n in nums:
            s.setdefault(n, 0)
            s[n] += 1

        ans = 0
        for n in nums:
            if n - 1 in s:
                ans = max(ans, s[n] + s[n - 1])
            if n + 1 in s:
                ans = max(ans, s[n] + s[n + 1])
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.findLHS([1,3,2,2,5,2,3,7]))
    print(sln.findLHS([1,2,3,4]))
    print(sln.findLHS([1,1,1,1]))