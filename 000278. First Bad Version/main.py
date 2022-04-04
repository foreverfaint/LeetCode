

def isBadVersion(version: int) -> bool:
    return version >= 1


class Solution:
    def _first(self, low, high) -> int:
        if low >= high:
            return low + (0 if isBadVersion(low) else 1)
        
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            return self._first(low, mid - 1)
        return self._first(mid + 1, high)

    def firstBadVersion(self, n: int) -> int:
        return self._first(1, n)


if __name__ == "__main__":
    sln = Solution()
    print(sln.firstBadVersion(1))
