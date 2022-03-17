from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        h = len(word1) + 1
        w = len(word2) + 1
        min_dist_1 = [0] * w
        min_dist_2 = [0] * w
        for y in range(0, h):
            for x in range(0, w):
                if y == 0:
                    min_dist_1[x] = x
                elif x == 0:
                    min_dist_1[0] = y
                else:
                    if word1[y - 1] == word2[x - 1]:
                        min_dist_1[x] = min_dist_2[x - 1]
                    else:
                        min_dist_1[x] = min(min_dist_2[x], min_dist_1[x - 1]) + 1
            for x in range(0, w):
                min_dist_2[x] = min_dist_1[x]
        return min_dist_1[-1]


if __name__ == "__main__":
    sln = Solution()
    print(sln.minDistance("sea", "eat"))
    print(sln.minDistance("leetcode", "etco"))