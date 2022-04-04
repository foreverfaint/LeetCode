from typing import List


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            s_ = set()
            for c in s:
                if c in s_:
                    return True
                s_.add(c)
            return False


        diff = []
        i = 0
        while i < len(s):
            if s[i] != goal[i]:
                diff.append(i)
            i += 1
        if len(diff) != 2:
            return False
        return s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
        


if __name__ == "__main__":
    sln = Solution()
    print(sln.buddyStrings(s = "ab", goal = "ba"))
    print(sln.buddyStrings(s = "ab", goal = "ab"))
    print(sln.buddyStrings(s = "aa", goal = "aa"))