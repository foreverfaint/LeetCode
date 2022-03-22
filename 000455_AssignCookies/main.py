from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_i = 0
        s_j = 0
        cnt = 0
        while g_i < len(g) and s_j < len(s):
            if g[g_i] <= s[s_j]:
                g_i += 1
                cnt += 1
            s_j += 1
        return cnt



if __name__ == "__main__":
    sln = Solution()
    print(sln.findContentChildren([1,2,3],[1,1]))
    print(sln.findContentChildren( [1,2], [1,2,3]))