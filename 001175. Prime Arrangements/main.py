from typing import List


class Solution:
    PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

    MAX = 10**9 + 7

    def permutations(self, x):
        return 1 if x == 1 else x * self.permutations(x - 1)

    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        n_primes = len([x for x in self.PRIMES if x <= n])
        n_left = n - n_primes
        return (self.permutations(n_primes) * self.permutations(n_left)) % self.MAX


if __name__ == "__main__":
    sln = Solution()
    print(sln.numPrimeArrangements(1))
    print(sln.numPrimeArrangements(5))
    print(sln.numPrimeArrangements(100))