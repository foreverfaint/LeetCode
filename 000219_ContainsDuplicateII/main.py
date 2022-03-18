from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dups = {}
        for i, x in enumerate(nums):
            dups.setdefault(x, [])
            arr = dups[x]
            if len(arr) > 0 and abs(i - arr[-1]) <= k:
                return True
            arr.append(i)
        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.containsNearbyDuplicate([1,2,3,1], 3))
    print(sln.containsNearbyDuplicate([1,0,1,1], 1))
    print(sln.containsNearbyDuplicate([1,2,3,1,2,3], 2))