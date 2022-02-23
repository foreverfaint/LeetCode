from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)

        r = []
        pre_x = None
        for x_loc, x in enumerate(nums):
            if x == pre_x:
                continue

            y_loc = x_loc + 1
            z_loc = len(nums) - 1
            while y_loc < z_loc:
                y = nums[y_loc]
                z = nums[z_loc]
                sum = x + y + z
                if x + y + z == 0:
                    r.append((x, y, z))

                if sum > 0:
                    z_loc -= 1

                if sum < 0:
                    y_loc += 1

                if sum == 0:
                    while nums[z_loc] == z and nums[y_loc] == y and y_loc < z_loc:
                        z_loc -= 1
                        y_loc += 1

            pre_x = x
        return r


def assert_list(expected, actual):
    def _h(sum_3):
        return ",".join([str(x) for x in sum_3])

    expected_set = set([_h(x) for x in expected])
    actual_set = set([_h(x) for x in actual])
    print(expected_set, actual_set)
    assert expected_set == actual_set


if __name__ == "__main__":
    assert_list([[-1, 0, 1]], Solution().threeSum([-1, 0, 1]))
    assert_list([[-1,-1,2],[-1,0,1]], Solution().threeSum([-1,0,1,2,-1,-4]))
    assert_list([[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]], Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
    assert_list([], Solution().threeSum([]))
    assert_list([], Solution().threeSum([0]))