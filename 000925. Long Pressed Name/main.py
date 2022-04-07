from typing import List


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l1 = len(name)
        l2 = len(typed)
        i = 0
        j = 0
        while i < l1 and j < l2:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        if j == l2 and i < l1:
            return False
        
        while j < l2:
            if j > 0 and typed[j] != typed[j - 1]:
                return False
            j += 1

        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.isLongPressedName("pyplrz", "ppyypllr"))
    print(sln.isLongPressedName("alexd", "ale"))
    print(sln.isLongPressedName("a", "b"))
    print(sln.isLongPressedName(name = "alex", typed = "aaleex"))
    print(sln.isLongPressedName(name = "saeed", typed = "ssaaedd"))