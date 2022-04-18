from typing import List


class Solution:
    def makeBouquets(self, bloomDay, m, k, minDays):
        i = 0
        isBloomFlag = [n <= minDays for n in bloomDay]
        # print(minDays, list(zip(bloomDay, isBloomFlag)), f"{k} flowers for {m} bouquets")
        for isBloom in isBloomFlag:
            if isBloom:
                i += 1
                if i == k:
                    m -= 1
                    if m == 0:
                        return True
                    i = 0
            else:
                i = 0
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = len(bloomDay)
        if l < m * k:
            return -1

        min_ = 1
        max_ = max(bloomDay)
        while min_ < max_:
            minDays = (min_ + max_) // 2
            canMakeBouquets = self.makeBouquets(bloomDay, m, k, minDays)
            # print(f"min_={min_}, minDays={minDays}, max_={max_}, canMakeBouquets={canMakeBouquets}")
            if canMakeBouquets:
                max_ = minDays
            else:
                min_ = minDays + 1
        return min_


if __name__ == "__main__":
    sln = Solution()
    print(sln.minDays(bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2))
    # print(sln.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
    # print(sln.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2))
    # print(sln.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))
