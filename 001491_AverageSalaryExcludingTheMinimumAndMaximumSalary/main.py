from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)


if __name__ == "__main__":
    sln = Solution()
    print(sln.average([4000,3000,1000,2000]))
    print(sln.average([3000,1000,2000]))