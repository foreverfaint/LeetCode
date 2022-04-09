from typing import List


class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = len(s)
        if l == 1:
            return s
        
        from collections import deque
        stack = deque()
        for c in s:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop()
                continue
            stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    sln = Solution()
    print(sln.removeDuplicates("abbaca"))
    print(sln.removeDuplicates("azxxzy"))