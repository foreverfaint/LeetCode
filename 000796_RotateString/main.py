from typing import List


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)


if __name__ == "__main__":
    sln = Solution()
    print(sln.rotateString(s = "abcde", goal = "cdeab"))
    print(sln.rotateString(s = "abcde", goal = "abced"))