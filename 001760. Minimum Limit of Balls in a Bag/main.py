from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low = 1
        high = max(nums)
        while low < high:
            mid = low + (high - low) // 2
            import math
            if sum([math.ceil(n / mid) - 1 for n in nums]) > maxOperations:
                low = mid + 1
            else:
                high = mid
        return low



if __name__ == "__main__":
    sln = Solution()
    print(sln.minimumSize(nums = [0], maxOperations = 1))
    print(sln.minimumSize(nums = [1], maxOperations = 1))
    print(sln.minimumSize(nums = [9], maxOperations = 2))
    print(sln.minimumSize(nums = [2,4,8,2], maxOperations = 4))
    print(sln.minimumSize(nums = [7,17], maxOperations = 2))