from typing import List


class Solution:
    months_in_normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_in_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def parse(self, s):
        fields = s.split("-")
        return int(fields[0]), int(fields[1]), int(fields[2])

    def days_until_now_in_this_year(self, y, m, d):
        months = self.months_in_leap_year if self.is_leap_year(y) else self.months_in_normal_year
        days = 0
        for i in range(m - 1):
            days += months[i]
        return days + d

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date2 < date1:
            date1, date2 = date2, date1
        y_1, m_1, d_1 = self.parse(date1)
        y_2, m_2, d_2 = self.parse(date2)

        days = 0
        for y in range(y_1, y_2):
            days += 366 if self.is_leap_year(y) else 365
        print( y_1, m_1, d_1, y_2, m_2, d_2, days)
        days += self.days_until_now_in_this_year(y_2, m_2, d_2)
        print(self.days_until_now_in_this_year(y_2, m_2, d_2))
        days -= self.days_until_now_in_this_year(y_1, m_1, d_1)
        print(self.days_until_now_in_this_year(y_1, m_1, d_1))
        return days


if __name__ == "__main__":
    sln = Solution()
    # print(sln.daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30"))
    # print(sln.daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))
    print(sln.daysBetweenDates(date1 = "2074-09-12", date2 = "1983-01-08"))

