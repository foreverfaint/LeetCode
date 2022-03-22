from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = [False] * (len(nums) + 1)
        for n in nums:
            ans[n] = True
        return [i for i in range(1, len(ans)) if not ans[i]]


if __name__ == "__main__":
    sln = Solution()
    print(sln.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(sln.findDisappearedNumbers([1,1]))