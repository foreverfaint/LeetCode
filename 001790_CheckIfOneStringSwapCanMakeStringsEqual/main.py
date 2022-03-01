from typing import List


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i = 0
        l = len(s1)
        k1, k2 = -1, -1
        while i < l:
            if s1[i] != s2[i]:
                if k1 == -1:
                    k1 = i
                elif k2 == -1:
                    k2 = i
                else:
                    return False
            i += 1

        if k1 == -1 and k2 == -1:
            return True
        elif k1 == -1 or k2 == -1:
            return False
        return s1[k1] == s2[k2] and s1[k2] == s2[k1]


if __name__ == "__main__":
    sln = Solution()
    print(sln.areAlmostEqual("qgqeg", "gqgeq"))
    print(sln.areAlmostEqual("bank", "kanb"))
    print(sln.areAlmostEqual("attack", "defend"))
    print(sln.areAlmostEqual("kelb", "kelb"))