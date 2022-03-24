from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ans = 0
        cur_ans = 0
        for n in nums:
            if n == 1:
                cur_ans += 1
                max_ans = max(cur_ans, max_ans)
            else:
                cur_ans = 0
        return max_ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.findMaxConsecutiveOnes([1,1,0,1,1,1]))
    print(sln.findMaxConsecutiveOnes([1,0,1,1,0,1]))