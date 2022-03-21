from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:
        m = {}
        for c in s:
            m.setdefault(c, 0)
            m[c] += 1
        ans = []
        for kv in sorted(m.items(), key=lambda kv: kv[1], reverse=True):
            ans.extend(kv[0] * kv[1])
        return "".join(ans)


if __name__ == "__main__":
    sln = Solution()
    print(sln.frequencySort("tree"))
    print(sln.frequencySort("cccaaa"))
    print(sln.frequencySort("Aabb"))