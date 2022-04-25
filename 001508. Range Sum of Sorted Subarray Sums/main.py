from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        import heapq
        q = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(q)
        ans = 0
        for i in range(1, right + 1):
            x, loc = heapq.heappop(q)
            if i >= left:
                ans += x
            if loc + 1 < len(nums):
                heapq.heappush(q, (x + nums[loc + 1], loc + 1))
        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    sln = Solution()
    print(sln.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5))
    print(sln.rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4))
    print(sln.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10))