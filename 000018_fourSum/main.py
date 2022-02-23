from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], loc_b: int, target: int):
        loc_c = loc_b + 1
        loc_d = len(nums) - 1

        while loc_c < loc_d:
            c = nums[loc_c]
            d = nums[loc_d]
            s = c + d

            if s == target:
                yield (c, d)
                while nums[loc_c] == c and nums[loc_d] == d and loc_c < loc_d:
                    loc_d -= 1
                    loc_c += 1
            elif s > target:
                loc_d -= 1
            elif s < target:
                loc_c += 1

    def threeSum(self, nums: List[int], loc_a: int, target: int):
        pre_b = None
        loc_b = loc_a + 1

        while loc_b < len(nums) - 2:
            b = nums[loc_b]
            if b == pre_b:
                loc_b += 1
                continue

            for c, d in self.twoSum(nums, loc_b, target - b):
                yield (b, c, d)
            
            pre_b = b
            loc_b += 1

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums = sorted(nums)

        r = []
        pre_a = None
        loc_a = 0
        while loc_a < len(nums) - 3:
            a = nums[loc_a]
            if a == pre_a:
                loc_a += 1
                continue

            for b, c, d in self.threeSum(nums, loc_a, target - a):
                r.append((a, b, c, d))

            pre_a = a
            loc_a += 1
        return r



def assert_list(expected, actual):
    def _h(lst):
        return ",".join([str(x) for x in lst])

    expected_set = set([_h(x) for x in expected])
    actual_set = set([_h(x) for x in actual])
    print(expected_set, actual_set)
    assert expected_set == actual_set


if __name__ == "__main__":
    assert_list([[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], Solution().fourSum([1,0,-1,0,-2,2], 0))
    assert_list([[2,2,2,2]], Solution().fourSum([2,2,2,2,2], 8))