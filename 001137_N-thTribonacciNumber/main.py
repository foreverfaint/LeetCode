class Solution:
    def _f(self, n, m):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        if n in m:
            return m[n]
        
        f = self._f(n-3, m) + self._f(n-2, m) + self._f(n-1, m)
        m[n] = f
        return f


    def tribonacci(self, n: int) -> int:
        m = {}
        return self._f(n, m)


if __name__ == "__main__":
    sln = Solution()
    print(sln.tribonacci(4))
    print(sln.tribonacci(25))