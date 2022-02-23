from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return []

        nums = sorted(nums)

        pre_x = None
        closest_value = sum(nums[:3])
        for x_loc, x in enumerate(nums):
            if x == pre_x:
                continue

            y_loc = x_loc + 1
            z_loc = len(nums) - 1
            while y_loc < z_loc:
                y = nums[y_loc]
                z = nums[z_loc]
                s = x + y + z
                if s - target == 0:
                    return target

                # print(x, "+", y, "+", z, "-", target, "=", s - target, "<", closest_value - target)
                if abs(s - target) < abs(closest_value - target):
                    closest_value = s

                if s > target:
                    z_loc -= 1

                if s < target:
                    y_loc += 1

        return closest_value


if __name__ == "__main__":
    assert 2 == Solution().threeSumClosest([-1,2,1,-4], 1)
    assert 0 == Solution().threeSumClosest([0,0,0], 1)
    assert 3 == Solution().threeSumClosest([0,1, 2], 0)