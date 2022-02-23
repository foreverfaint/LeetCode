
class Solution:
    def _climbs(self, m, n):
        if n == 1:
            return 1

        if n == 2:
            return 2

        r = m.get(n)
        if r:
            return r

        r = self._climbs(m, n - 1) + self._climbs(m, n - 2)
        m[n] = r
        return r

    def climbStairs(self, n: int) -> int:
        m = {}
        return self._climbs(m, n)


if __name__ == "__main__":
    sln = Solution()
    print(sln.climbStairs(2))
    print(sln.climbStairs(3))
    print(sln.climbStairs(4))
    print(sln.climbStairs(5))
    print(sln.climbStairs(6))