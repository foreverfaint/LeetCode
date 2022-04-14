from typing import List


class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if 'a' <= c <= 'z']
        l_letters = len(letters)

        digits = [c for c in s if '0' <= c <= '9']
        l_digits = len(digits)
        
        if abs(l_letters - l_digits) > 1:
            return ""
        
        if l_letters > l_digits:
            return "".join([a + b for a, b in zip(letters[:-1], digits)]) + letters[-1]
        elif l_letters < l_digits:
            return digits[-1] + "".join([a + b for a, b in zip(letters, digits[:-1])])
        else:
            return "".join([a + b for a, b in zip(letters, digits)])
        
        

if __name__ == "__main__":
    sln = Solution()
    print(sln.reformat("a0b1c2"))
    print(sln.reformat("a0b1ck2"))
    print(sln.reformat("a0b1c52"))
    print(sln.reformat("leetcode"))
    print(sln.reformat("1229857369"))