from typing import List


class Solution:
    def _rob(self, nums, n, m):
        if n == 0:
            return nums[0]

        if n == 1:
            return max(nums[0], nums[1])

        r = m.get(n)
        if not r:
            r = max(self._rob(nums, n - 2, m) + nums[n], self._rob(nums, n - 1, m))
            m[n] = r

        return r

    def rob(self, nums: List[int]) -> int:
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
        return self._rob(nums, i - 1, {})


if __name__ == "__main__":
    sln = Solution()
    print(sln.rob([2,0,0,7,9,3,1]))
    print(sln.rob([0,0,0,2,0,0,7,9,3,1]))
    print(sln.rob([1]))
    print(sln.rob([1,2]))
    print(sln.rob([1,2,3]))
    print(sln.rob([1,2,3,1]))
    print(sln.rob([2,7,9,3,1]))