from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        ans = [n for n, f in Counter(arr).most_common() if n == f]
        return ans[0] if ans else -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.findLucky([2,2,3,4]))
    print(sln.findLucky([1,2,2,3,3,3]))
    print(sln.findLucky([2,2,2,3,3]))