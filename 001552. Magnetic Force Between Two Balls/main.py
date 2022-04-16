
from typing import List


class Solution:
    def locate(self, position, k):
        used , curr_pos = 1, position[0]
        for i in range(1, len(position)):
            if position[i] - curr_pos >= k:
                used += 1
                curr_pos = position[i]
        return used

    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        low = 0
        high = position[-1] - position[0]
        while low < high:
            # https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/794066/Simple-Explanation
            k = low + (high - low) // 2 + 1 # +1 avoid low == mid < high forever
            used = self.locate(position, k)
            # print(f"low[{low}] <= k[{k}] <= high[{high}], used={used}, expected={m}")
            if used >= m:
                low = k
            else:
                high = k - 1
        return low


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxDistance(position = [79,74,57,22], m = 4))
    print(sln.maxDistance(position = [1,2,3,4,7], m = 3))
    print(sln.maxDistance(position = [5,4,3,2,1,1000000000], m = 2))