from typing import List


class Solution:
    def _rob(self, nums, low, high, m):
        if high == low:
            return nums[low]

        if high == low + 1:
            return max(nums[low], nums[low + 1])

        r = m.get((low, high))
        if not r:
            r = max(self._rob(nums, low, high - 2, m) + nums[high], self._rob(nums, low, high - 1, m))
            m[(low, high)] = r

        return r

    def rob(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        i = 1
        j = 1
        l = len(nums)
        while j < l:
            nums[i] = nums[j]
            if nums[i] == 0 and nums[i - 1] == 0:
                j += 1
            else:
                j += 1
                i += 1

        if nums[i - 1] != 0 and nums[l - 1] == 0:
            i += 1
        
        if nums[0] == 0 and nums[i - 1] == 0:
            i -= 1

        return max(self._rob(nums, 1, i - 1, {}), self._rob(nums, 0, i - 2, {}))


if __name__ == "__main__":
    sln = Solution()
    print(sln.rob([1]))
    print(sln.rob([0,0]))
    print(sln.rob([1,2,3,0,0]))
    print(sln.rob([0,0,1,2,3,0,0]))
    print(sln.rob([2,3,2]))
    print(sln.rob([1,2,3,1]))
    print(sln.rob([1,2,3]))