from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            m.setdefault(i, 0)
            m[i] += i
        m = sorted(m.items(), key=lambda kv: kv[0])

        l = len(m)
        if l == 0:
            return 0
        elif l == 1:
            return m[0][1]

        r_2 = m[0][1]
        r_1 = max(m[0][1], m[1][1]) if m[0][0] + 1 == m[1][0] else (m[0][1] + m[1][1])
        max_earn = r_1
        i = 2
        while i < l:
            max_earn = max(r_1, m[i][1] + r_2) if m[i - 1][0] + 1 == m[i][0] else (r_1 + m[i][1])
            r_2 = r_1
            r_1 = max_earn
            i += 1

        return max_earn
            



if __name__ == "__main__":
    sln = Solution()
    print(sln.deleteAndEarn([3,4,2]))
    print(sln.deleteAndEarn([2,2,3,3,3,4]))