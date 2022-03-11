from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 0

        trust_somebody = set()

        from collections import defaultdict
        trusted = defaultdict(int)
        for e in trust:
            trusted[e[1]] +=1
            trust_somebody.add(e[0])

        for k, v in trusted.items():
            if v == n - 1 and k not in trust_somebody:
                return k
        return -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.findJudge(2, [[1, 2]]))
    print(sln.findJudge(3, [[1, 3], [2, 3]]))
    print(sln.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
