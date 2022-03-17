from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        max_ = [1] * l  # the longest sequence to ith
        cnt_ = [1] * l  # how many ways to the longest sequence to ith.

        # Check every pair:
        # - any pair (nums[i], nums[i]) satisfy "<", it may contribute to nums[:i+1] longest sequences + 1 in
        #   - either make it longer if max_[j] + 1 > max_[i]
        #   - or make more longest sequences if max_[j] + 1 == max_[i]
        for i in range(l):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if max_[j] + 1 > max_[i]:
                    max_[i] = max_[j] + 1
                    cnt_[i] = cnt_[j]
                elif max_[j] + 1 == max_[i]:
                    cnt_[i] += cnt_[j]

        max_r = max(max_)
        cnt_r = 0
        for i in range(l):
            if max_[i] == max_r:
                cnt_r += cnt_[i]
        return cnt_r


if __name__ == "__main__":
    sln = Solution()
    print(sln.findNumberOfLIS([1, 3, 5, 4, 7]))
    print(sln.findNumberOfLIS([2, 2, 2, 2, 2]))
