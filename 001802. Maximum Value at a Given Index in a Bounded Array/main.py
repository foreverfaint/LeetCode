from typing import List


class Solution:
    def foo(self, mid, n, index):
        l = mid
        r = max(1, mid - (n - index) + 1)
        s = (l + r) * (l - r + 1) // 2
        if n - index > mid:
            s += n - index - mid

        l = max(1, mid - index)
        r = mid
        s += (l + r) * (r - l + 1) // 2
        if index >= mid:
            s += index - mid + 1

        return s - mid

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low = 1
        high = maxSum
        while low < high:
            mid = (low + high) // 2
            s = self.foo(mid, n, index)
            print(f"low={low}, mid={mid}, high={high} => sum={s} <= {maxSum}")
            if s <= maxSum:
                low = mid + 1
            else:
                high = mid
        return low if self.foo(low, n, index) <= maxSum else low - 1


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxValue(n = 4, index = 2,  maxSum = 6))
    print(sln.maxValue(n = 6, index = 1,  maxSum = 10))