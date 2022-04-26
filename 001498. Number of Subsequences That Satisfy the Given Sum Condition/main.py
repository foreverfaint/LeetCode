from typing import List

from cv2 import sort


class Solution:
    def bs(self, arr, target):
        low = 0
        high = len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def bs2(self, arr, target):
        low = 0
        high = len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low

    def numSubseq2(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        start = self.bs(nums, target)
        res = 0
        i = 0
        while i < start:
            n = target - nums[i]
            if n < nums[i]:
                break

            end = self.bs2(nums[i:start], n)
            res += (2 ** (end - 1)) % (10 ** 9 + 7)
            i += 1
            
        return res % (10 ** 9 + 7)

    def numSubseq(self, nums, target):
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod


if __name__ == "__main__":
    sln = Solution()
    print(sln.numSubseq(nums = [3,5,6,7], target = 9))
    print(sln.numSubseq(nums = [3,3,6,8], target = 10))
    print(sln.numSubseq(nums = [2,3,3,4,6,7], target = 12))