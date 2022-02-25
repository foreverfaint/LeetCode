from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        r = []
        for i in range(len(nums)):
            t = nums[i]
            nums[i] = nums[0]
            for sub_r in self.permute(nums[1:]):
                r.append([t] + sub_r)
            nums[i]  = t
        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.permute([1]))
    print(sln.permute([0,1]))
    print(sln.permute([1,2,3]))