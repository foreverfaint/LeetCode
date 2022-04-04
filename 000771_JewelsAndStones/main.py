from typing import List


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(list(jewels))
        return len([stone for stone in stones if stone in jewels])


if __name__ == "__main__":
    sln = Solution()
    print(sln.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
    print(sln.numJewelsInStones(jewels = "z", stones = "ZZ"))