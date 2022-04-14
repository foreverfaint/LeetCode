from typing import List


class Solution:
    def sortString(self, s: str) -> str:
        m = {}
        for c in s:
            m.setdefault(c, 0)
            m[c] += 1

        m = sorted(m.items(), key=lambda kv: kv[0])
        ans = []
        while any([cnt > 0 for _, cnt in m]):
            i = 0
            while i < len(m):
                c, cnt = m[i]
                if cnt > 0:
                    ans.append(c)
                    m[i] = (c, cnt - 1)
                i += 1

            j = len(m) - 1
            while j >= 0:
                c, cnt = m[j]
                if cnt > 0:
                    ans.append(c)
                    m[j] = (c, cnt - 1)
                j -= 1
        return "".join(ans)

if __name__ == "__main__":
    sln = Solution()
    print(sln.sortString("aaaabbbbcccc"))
    print(sln.sortString("rat"))