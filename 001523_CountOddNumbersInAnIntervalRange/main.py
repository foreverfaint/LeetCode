
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low_is_even = (low % 2 == 0)
        high_is_even = (high % 2 == 0)
        r = (high - low) // 2
        if low_is_even and high_is_even:
            return r
        elif low_is_even:
            return r + 1
        elif high_is_even:
            return r + 1
        else:
            return r + 1


if __name__ == "__main__":
    sln = Solution()
    print(sln.countOdds(3, 7))
    print(sln.countOdds(8, 10))
    print(sln.countOdds(8, 11))
    print(sln.countOdds(7, 10))