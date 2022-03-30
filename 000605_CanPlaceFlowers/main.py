from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            prev_ok = i == 0 or flowerbed[i - 1] == 0
            next_ok = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            curr_ok = flowerbed[i] == 0
            if prev_ok and next_ok and curr_ok:
                n -= 1
                flowerbed[i] = 1
        return n <= 0


if __name__ == "__main__":
    sln = Solution()
    print(sln.canPlaceFlowers(flowerbed = [1,0,0,0,0,1], n = 2))
    print(sln.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
    print(sln.canPlaceFlowers(flowerbed = [1,0,1,0,1,0,1], n = 1))
    print(sln.canPlaceFlowers(flowerbed = [0,0,0,1], n = 1))
    print(sln.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
    print(sln.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))