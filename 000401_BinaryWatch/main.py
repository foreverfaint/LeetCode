from typing import List


class Solution:
    def countBits(self, n):
        c = 0
        while n > 0:
            c += 1 if n % 2 == 1 else 0
            n >>= 1
        return c

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn >= 9:
            return []

        ans = []
        hours = [self.countBits(n) for n in range(12)]
        minutes = [self.countBits(n) for n in range(60)]
        for hour, i in enumerate(hours):
            for minute, j in enumerate(minutes):
                if i + j == turnedOn:
                    ans.append(f"{hour}:{minute:02d}")
        return ans


if __name__ == "__main__":
    sln = Solution()
    
    print(sln.readBinaryWatch(1))
    print(sln.readBinaryWatch(2))
    print(sln.readBinaryWatch(3))
    print(sln.readBinaryWatch(4))
    print(sln.readBinaryWatch(5))
    print(sln.readBinaryWatch(6))
    print(sln.readBinaryWatch(7))
    print(sln.readBinaryWatch(8))
    print(sln.readBinaryWatch(9))