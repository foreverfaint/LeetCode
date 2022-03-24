from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [(i, x) for i, x in enumerate(score)]
        score = sorted(score, key=lambda kv: kv[1], reverse=True)

        def _(i, kv):
            if i == 0:
                return (kv[0], "Gold Medal")
            if i == 1:
                return (kv[0], "Silver Medal")
            if i == 2:
                return (kv[0], "Bronze Medal")
            return (kv[0], str(i + 1))                

        score = [_(i, kv) for i, kv in enumerate(score)]
        return [kv[1] for kv in sorted(score, key=lambda kv: kv[0])]



if __name__ == "__main__":
    sln = Solution()
    print(sln.findRelativeRanks([5,4,3,2,1]))
    print(sln.findRelativeRanks([10,3,8,9,4]))