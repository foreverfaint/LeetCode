class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if top == '(' and c != ')':
                    return False
                if top == '[' and c != ']':
                    return False
                if top == '{' and c != '}':
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    sln= Solution()
    print(sln.isValid("()"))
    print(sln.isValid("([{}])"))
    print(sln.isValid("([]){}"))
    print(sln.isValid("(}"))
    print(sln.isValid("({}"))