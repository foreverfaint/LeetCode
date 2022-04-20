from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
    print(sln.singleNonDuplicate([3,3,7,7,10,11,11]))