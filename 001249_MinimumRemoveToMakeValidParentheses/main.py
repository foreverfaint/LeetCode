from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        from collections import deque

        stack = deque()
        for c1 in s:
            if c1 == ')':
                s = ""
                while len(stack) > 0:
                    c2 = stack.pop()
                    if c2 == "(":
                        stack.append(f"({s})")
                        break
                    s = c2 + s

                if len(stack) == 0:
                    stack.append(s)
            else:
                stack.append(c1)

        s = ""
        while len(stack) > 0:
            c4 = stack.pop()
            if c4 != "(":
                s = c4 + s
        return s


if __name__ == "__main__":
    sln = Solution()
    print(sln.minRemoveToMakeValid("("))
    print(sln.minRemoveToMakeValid("a("))
    print(sln.minRemoveToMakeValid("a(b"))
    print(sln.minRemoveToMakeValid("a(b)c"))
    print(sln.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(sln.minRemoveToMakeValid("a)b(c)d"))
    print(sln.minRemoveToMakeValid("))(("))