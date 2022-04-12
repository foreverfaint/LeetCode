from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        nums = sorted(nums)
        ans = 0
        for k in range(2, l):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                elif nums[i] + nums[j] <= nums[k]:
                    i += 1
        return ans
        

if __name__ == "__main__":
    sln = Solution()
    print(sln.triangleNumber([0,0,0])) # 0
    print(sln.triangleNumber([2,2,3,4])) # 3
    print(sln.triangleNumber([4,2,3,4])) # 4
    print(sln.triangleNumber([54,98,9,98,5,61,54,83]))  # 26