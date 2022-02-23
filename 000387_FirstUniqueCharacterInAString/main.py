from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for i, c in enumerate(iter(s)):
            m.setdefault(c, (0, i))
            n, first_loc = m[c]
            m[c] = (n + 1, first_loc)
        
        s_lst = [kv[1] for kv in m.items() if kv[1][0] == 1]
        s_lst = sorted(s_lst, key=lambda kv: kv[1])
        return -1 if not s_lst else s_lst[0][1]



if __name__ == "__main__":
    sln = Solution()
    print(sln.firstUniqChar("leetcode"))
    print(sln.firstUniqChar("loveleetcode"))
    print(sln.firstUniqChar("aabb"))