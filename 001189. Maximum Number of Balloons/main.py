
from typing import List


class Solution:
    def map(self, text):
        m = {}
        for c in text:
            m.setdefault(c, 0)
            m[c] += 1
        return m

    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = self.map("balloon")
        m = self.map(text)

        ans = 0
        while True:
            for c, cnt in balloon.items():
                t_cnt = m.get(c, 0)
                if t_cnt >= cnt:
                    m[c] = t_cnt - cnt
                else:
                    return ans
            ans += 1


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxNumberOfBalloons("nlaebolko"))
    print(sln.maxNumberOfBalloons("loonbalxballpoon"))
    print(sln.maxNumberOfBalloons("leetcode"))