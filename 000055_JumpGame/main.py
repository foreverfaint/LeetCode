from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = -1
        i = 0
        l = len(nums)
        while True:
            max_jump = max(max_jump, i + nums[i])
            if max_jump >= l - 1:
                return True
            elif max_jump <= i:
                break
            i += 1
        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.canJump([2,3,1,1,4]))
    print(sln.canJump([3,2,1,0,4]))