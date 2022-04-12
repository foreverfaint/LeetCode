from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        l = len(dominoes)
        m = {}
        for i in range(l):
            dominoes[i] = (min(dominoes[i][0], dominoes[i][1]), max(dominoes[i][0], dominoes[i][1]))
            m.setdefault(dominoes[i], 0)
            m[dominoes[i]] += 1

        ans = 0
        for _, cnt in m.items():
            if cnt > 1:
                ans += cnt * (cnt - 1) // 2
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
    print(sln.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))