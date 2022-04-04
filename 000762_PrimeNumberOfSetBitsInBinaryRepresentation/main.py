from typing import List


class Solution:
    def numberOfSetBits(self, n):
        ans = 0
        while n > 0:
            ans += 1 if n % 2 == 1 else 0
            n >>= 1
        return ans

    def genPrimeSet(self, n):
        ans = set()
        for i in range(2, n):
            import math
            if all([i % j != 0 for j in range(2, math.ceil(math.sqrt(i)) + 1) if i != j]):
                ans.add(i)
        return ans

    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = self.genPrimeSet(32)
        ans = 0
        for i in range(left, right + 1):
            k = self.numberOfSetBits(i)
            if k in primes:
                ans += 1
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.countPrimeSetBits(6, 10))
    print(sln.countPrimeSetBits(10, 15))