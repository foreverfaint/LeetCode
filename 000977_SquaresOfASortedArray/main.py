from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] >= 0:
                break;
            i += 1

        j = i
        i = i -1
        new_nums = []
        nums = [x * x for x in nums]
        while i > -1 and j < l:
            if nums[i] < nums[j]:
                new_nums.append(nums[i])
                i -= 1
            else:
                new_nums.append(nums[j])
                j += 1

        while i > -1:
            new_nums.append(nums[i])
            i -= 1

        while j < l:
            new_nums.append(nums[j])
            j += 1

        return new_nums
    


if __name__ == "__main__":
    sln = Solution()
    print(sln.sortedSquares([-4,-1,0,3,10]))
    print(sln.sortedSquares([-7,-3,2,3,11]))
    print(sln.sortedSquares([-7,-3]))
    print(sln.sortedSquares([2,3,11]))
    print(sln.sortedSquares([]))
    