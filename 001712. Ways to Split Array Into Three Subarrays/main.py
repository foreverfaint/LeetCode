from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        l = len(nums)
        left_acc = [0] * l
        left_acc[0] = nums[0]
        for i in range(1, l):
            left_acc[i] = left_acc[i - 1] + nums[i]

        ans = 0
        left_b, right_min_b, right_max_b = 0, 0, 0
        while left_b < l - 2:
            left = left_acc[left_b]

            right_min_b = max(left_b + 1, right_min_b)
            while right_min_b < l - 1 and left_acc[right_min_b] < 2 * left:
                right_min_b += 1

            right_max_b = max(right_min_b, right_max_b)
            while right_max_b < l - 1 and (left_acc[right_max_b] - left) <= (left_acc[-1] - left_acc[right_max_b]):
                right_max_b += 1

            # right_max_b over bound with 1
            # print(f"left=({left_b}, {nums[:left_b + 1]}), right=({right_min_b}, {nums[left_b + 1: right_min_b + 1]}-{nums[right_min_b + 1:]}) ~ ({right_max_b}, {nums[left_b + 1: right_max_b]}-{nums[right_max_b:]})")
            ans = (ans + right_max_b - right_min_b) % 1000000007

            left_b += 1
        return ans


if __name__ == "__main__":
    sln = Solution()

    print(sln.waysToSplit(nums = [4,2,3,0,3,5,3,12]))
    print(sln.waysToSplit(nums = [0,3,3]))
    print(sln.waysToSplit(nums = [1,1,1]))
    print(sln.waysToSplit(nums = [1,2,2,2,5,0]))
    print(sln.waysToSplit(nums = [3,2,1]))