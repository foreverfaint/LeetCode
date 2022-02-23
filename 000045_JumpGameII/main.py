from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        
        jumps = [l for _ in range(l)]
        jumps[0] = 0

        i = 0
        while i < l:
            for j in range(i + 1, min(i + 1 + nums[i], l)):
                jumps[j] = min(jumps[j], jumps[i] + 1)
                # print(i, j, jumps)
            i += 1

        return jumps[-1]


if __name__ == "__main__":
    sln = Solution()
    print(sln.jump([2,3,1,1,4]))
    print(sln.jump([2,3,0,1,4]))