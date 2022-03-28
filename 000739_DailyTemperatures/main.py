import enum
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        from collections import deque
        stack = deque()
        for i, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(sln.dailyTemperatures([30,40,50,60]))
    print(sln.dailyTemperatures([30,60,90]))