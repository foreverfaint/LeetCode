from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {n: i + 1 for i, n in enumerate(sorted(list(set(arr))))}
        return [rank.get(n) for n in arr]


if __name__ == "__main__":
    sln = Solution()
    print(sln.arrayRankTransform([40,10,20,30]))
    print(sln.arrayRankTransform([100,100,100]))
    print(sln.arrayRankTransform([37,12,28,9,100,56,80,5,12]))