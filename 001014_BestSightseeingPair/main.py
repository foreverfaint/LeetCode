from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # The key is 2 layers DP
        # the first DP is the value of the first sight, since the larger first sight value generates a larger final score.
        # the second DP is score
        max_1 = values[0]
        max_2 = values[1] + max_1 - 1
        i = 1
        l = len(values)
        while i < l - 1:
            max_1 = max(max_1, values[i] + i)
            max_2 = max(max_2, max_1 + values[i + 1] - i - 1)
            i += 1
        return max(max_2, max_1 + values[l - 1] - l + 1)
                 

if __name__ == "__main__":
    sln = Solution()
    print(sln.maxScoreSightseeingPair([8,1,5,2,6]))
    print(sln.maxScoreSightseeingPair([1,2]))