from typing import List


guess = lambda x: -1


class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n

        l = 1
        h = n
        while True:
            x = l + (h - l) // 2
            flag = guess(x)
            if flag == 0:
                return x
            elif flag < 0:
                h = x - 1
            else:
                l = x + 1


if __name__ == "__main__":
    sln = Solution()

    guess = lambda x: -1 if x > 6 else (0 if x == 6 else 1)
    print(sln.guessNumber(10))

    guess = lambda x: -1 if x > 1 else (0 if x == 1 else 1)
    print(sln.guessNumber(1))

    guess = lambda x: -1 if x > 1 else (0 if x == 1 else 1)
    print(sln.guessNumber(2))

    guess = lambda x: -1 if x > 2 else (0 if x == 2 else 1)
    print(sln.guessNumber(2))