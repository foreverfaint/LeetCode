from typing import List

 
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        min_ = 1
        max_ = max(nums)
        while min_ < max_:
            divisor = (max_ + min_) // 2
            import math
            sum_ = sum([math.ceil(n / divisor) for n in nums])
            if sum_ > threshold:
                min_ = divisor + 1
            else:
                max_ = divisor
        return min_


if __name__ == "__main__":
    sln = Solution()
    # 5
    print(sln.smallestDivisor(nums = [1,2,5,9], threshold = 6))
    # 44
    print(sln.smallestDivisor(nums = [44,22,33,11,1], threshold = 5))
    # 1
    print(sln.smallestDivisor(nums = [21212,10101,12121], threshold = 1000000))


