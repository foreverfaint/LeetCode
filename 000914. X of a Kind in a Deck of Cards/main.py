from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        m = {}
        for n in deck:
            m.setdefault(n, 0)
            m[n] += 1

        min_ = min(list(m.values()))
        if min_ < 2:
            return False

        for div in range(2, min_ + 1):
            if all([val % div == 0 for val in m.values()]):
                return True
        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))
    print(sln.hasGroupsSizeX([1,1,2,2,2,2]))
    print(sln.hasGroupsSizeX([1,2,3,4,4,3,2,1]))
    print(sln.hasGroupsSizeX([1,1,1,2,2,2,3,3]))