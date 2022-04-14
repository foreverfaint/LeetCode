from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        m = {}
        k = len(arr) // 4 + 1
        for n in arr:
            m.setdefault(n, 0)
            m[n] += 1
            if m[n] >= k:
                return n

if __name__ == "__main__":
    sln = Solution()
    print(sln.findSpecialInteger([1,2,2,6,6,6,6,7,10]))
    print(sln.findSpecialInteger([1, 1]))