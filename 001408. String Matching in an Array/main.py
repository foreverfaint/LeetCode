from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = [w for _, w in sorted([(len(w), w) for w in words])]
        ans = []
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.stringMatching(["mass","as","hero","superhero"]))
    print(sln.stringMatching(["leetcode","et","code"]))
    print(sln.stringMatching(["blue","green","bu"]))