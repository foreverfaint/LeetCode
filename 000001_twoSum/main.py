from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        loc = {x: i for i, x in enumerate(nums)}
        for i, x in enumerate(nums):
            y = target - x
            j = loc.get(y)
            if j and i != j:
                return [i, j]


if __name__ == "__main__":
    assert [0,1] == Solution().twoSum([2,7,11,15], 9)
    assert [1,2] == Solution().twoSum([3,2,4], 6)
    assert [0,1] == Solution().twoSum([3,3], 6)