from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        final = (aliceSum + bobSum) // 2
        if aliceSum == final:
            return [0, 0]
        elif aliceSum < final:
            diff = final - aliceSum
            bobs = set(bobSizes)
            for i in aliceSizes:
                if (i + diff) in bobs:
                    return [i, i + diff]
        else:
            diff = final - bobSum
            alices = set(aliceSizes)
            for i in bobSizes:
                if (i + diff) in alices:
                    return [i + diff, i]


if __name__ == "__main__":
    sln = Solution()
    print(sln.fairCandySwap(aliceSizes = [1,1], bobSizes = [2,2]))
    print(sln.fairCandySwap(aliceSizes = [1,2], bobSizes = [2,3]))
    print(sln.fairCandySwap(aliceSizes = [2], bobSizes = [1,3]))