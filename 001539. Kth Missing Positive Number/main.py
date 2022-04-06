from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        n = 1
        while i < len(arr):
            if n < arr[i]:
                k -= 1
                if k == 0:
                    return n
            else:
                i += 1
            n += 1
        if k > 0:
            n += k - 1
        return n


if __name__ == "__main__":
    sln = Solution()
    print(sln.findKthPositive(arr = [2,3,4,7,11], k = 5))
    print(sln.findKthPositive(arr = [1,2,3,4], k = 2))