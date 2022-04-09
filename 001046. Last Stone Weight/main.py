from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            if stones[-2] == stones[-1]:
                stones = stones[:-2]
            elif stones[-2] < stones[-1]:
                diff = stones[-1] - stones[-2]
                stones = stones[:-2] + [diff]
        return stones[0] if len(stones) == 1 else 0


if __name__ == "__main__":
    sln = Solution()
    print(sln.lastStoneWeight([2,7,4,1,8,1]))
    print(sln.lastStoneWeight([1]))
    print(sln.lastStoneWeight([1, 1]))
    print(sln.lastStoneWeight([2, 1, 1]))