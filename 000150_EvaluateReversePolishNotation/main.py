from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        stack = deque()
        for s in tokens:
            if s in "+-*/":
                n2 = stack.pop()
                n1 = stack.pop()
                if s == "+":
                    stack.append(n1 + n2)
                elif s == "-":
                    stack.append(n1 - n2)
                elif s == "*":
                    stack.append(n1 * n2)
                elif s == "/":
                    stack.append(int(n1 / n2))
            else:
                stack.append(int(s))
        return stack.pop()



if __name__ == "__main__":
    sln = Solution()
    print(sln.evalRPN(["2","1","+","3","*"]))
    print(sln.evalRPN(["4","13","5","/","+"]))
    print(sln.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))