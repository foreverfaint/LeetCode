from typing import List


class Solution:
    def countLargestGroup(self, n: int) -> int:
        m = {}
        for i in range(1, n + 1):
            x = 0
            j = i
            while i > 0:
                x += i % 10
                i = i // 10
            m.setdefault(x, [])
            m[x].append(j)

        size = [len(lst) for _, lst in m.items()]
        max_ = max(size)
        return len([x for x in size if x == max_])

if __name__ == "__main__":
    sln = Solution()
    print(sln.countLargestGroup(13))
    print(sln.countLargestGroup(2))