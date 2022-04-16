from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            k = low + (high - low) // 2
            import math
            hours = sum([math.ceil(pile / k) for pile in piles])
            if hours <= h:
                high = k
            else:
                low = k + 1
        return low
        


if __name__ == "__main__":
    sln = Solution()
    print(sln.minEatingSpeed(piles = [3,6,7,11], h = 8))
    print(sln.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
    print(sln.minEatingSpeed(piles = [30,11,23,4,20], h = 6))