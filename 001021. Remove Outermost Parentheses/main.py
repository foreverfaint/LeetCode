from typing import List


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        from collections import deque
        stack = deque()
        stack.append(s[0])

        for i in range(1, len(s)):
            if s[i] == ")":
                subs = ")"
                while True:
                    top = stack.pop()
                    subs = top + subs
                    if top == "(":
                        stack.append(subs)
                        break
            else:
                stack.append(s[i])
        
        return "".join(subs[1:-1] for subs in stack)

if __name__ == "__main__":
    sln = Solution()
    print(sln.removeOuterParentheses("(()())(())"))
    print(sln.removeOuterParentheses("(()())(())(()(()))"))
    print(sln.removeOuterParentheses("()()"))