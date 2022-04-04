from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_v = nums[0]
        max_i = 0
        for i in range(1, len(nums)):
            if nums[i] > max_v:
                max_v = nums[i]
                max_i = i
        return max_i if all([n * 2 <= max_v for n in nums if n != max_v]) else -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.dominantIndex([3,6,1,0]))
    print(sln.dominantIndex([1,2,3,4]))
    print(sln.dominantIndex([1]))