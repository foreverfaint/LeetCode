from typing import List


class Solution:
    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def dayOfYear(self, date: str) -> int:
        year, month, day = [int(x) for x in date.split("-")]
        ans = day
        for i in range(month - 1):
            ans += 29 if i == 1 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else self.daysInMonths[i]
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.dayOfYear("2019-01-09"))
    print(sln.dayOfYear("2019-02-10"))
    print(sln.dayOfYear("2000-12-04"))
