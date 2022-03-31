from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        from collections import deque
        stack = deque()
        for op in ops:
            if op == "D":
                n = stack.pop()
                stack.append(n)
                stack.append(n * 2)
            elif op == "C":
                stack.pop()
            elif op == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2)
                stack.append(n1)
                stack.append(n1 + n2)
            else:
                stack.append(int(op))

        s = 0
        while len(stack) > 0:
            n = stack.pop()
            s += n
        return s



if __name__ == "__main__":
    sln = Solution()
    print(sln.calPoints(["5","2","C","D","+"]))
    print(sln.calPoints(["5","-2","4","C","D","9","+","+"]))
    print(sln.calPoints(["1"]))