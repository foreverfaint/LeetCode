from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)

        if l == 0:
            return

        if l == 1:
            return

        i = 0
        j = l - 1
        while i < j:
            t = s[i]
            s[i] = s[j]
            s[j] = t
            i += 1
            j -= 1
        


if __name__ == "__main__":
    sln = Solution()

    s = []
    sln.reverseString(s)
    print(s)

    s = ["h"]
    sln.reverseString(s)
    print(s)        

    s = ["h","e","l","l","o"]
    sln.reverseString(s)
    print(s)

    s = ["H","a","n","n","a","h"]
    sln.reverseString(s)
    print(s)