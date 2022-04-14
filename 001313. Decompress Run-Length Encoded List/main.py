from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            ans.extend([val] * freq)
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.decompressRLElist([1,2,3,4]))
    print(sln.decompressRLElist([1,1,2,3]))