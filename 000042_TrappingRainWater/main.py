
from re import L
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        right_max = [0] * l
        left_max = [0] * l

        i = 1
        while i < l:
            left_max[i] = max(left_max[i - 1], height[i - 1])
            i += 1

        i = l - 2
        while i >= 0:  
            right_max[i] = max(right_max[i + 1], height[i + 1])
            i -= 1

        cap = 0
        i = 0
        while i < l:
            cap += max(0, min(left_max[i], right_max[i]) - height[i])
            i += 1
        return cap


if __name__ == "__main__":
    sln = Solution()
    print(sln.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(sln.trap([4,2,0,3,2,5]))