from typing import List


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # a larger number & a small number => a smaller number
        while right > left:
            right = right & (right - 1)
        return left & right


if __name__ == "__main__":
    sln = Solution()
    print(sln.rangeBitwiseAnd(2, 2))
    print(sln.rangeBitwiseAnd(5, 7))
    print(sln.rangeBitwiseAnd(0, 0))
    print(sln.rangeBitwiseAnd(1, 2147483647))