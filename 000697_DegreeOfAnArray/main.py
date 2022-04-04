from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        m = {}
        for i, n in enumerate(nums):
            m.setdefault(n, (float("inf"), 0, 0))
            m[n] = (min(i, m[n][0]), max(i, m[n][1]), m[n][2] + 1)

        s = [(v[2], v[1] - v[0] + 1) for _, v in m.items()]
        max_ = max([t[0] for t in s])
        s = [t[1] for t in s if t[0] == max_]
        return min(s)
        

if __name__ == "__main__":
    sln = Solution()
    print(sln.findShortestSubArray([1,1,2,2,2,1]))
    print(sln.findShortestSubArray([1,2,2,3,1]))
    print(sln.findShortestSubArray([1,2,2,3,1,4,2]))