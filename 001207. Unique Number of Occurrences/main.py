from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        val = Counter(arr).values()
        return len(val) == len(set(val))

if __name__ == "__main__":
    sln = Solution()
    print(sln.uniqueOccurrences([1,2,2,1,1,3]))
    print(sln.uniqueOccurrences([1,2]))
    print(sln.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))