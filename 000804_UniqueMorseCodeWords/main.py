from typing import List


class Solution:
    M = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def convert(self, w):
        s = ""
        for c in w:
            s += self.M[ord(c) - ord('a')]
        return s

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = set()
        for w in words:
            ans.add(self.convert(w))
        return len(ans)


if __name__ == "__main__":
    sln = Solution()
    print(sln.uniqueMorseRepresentations(["gin","zen","gig","msg"]))
    print(sln.uniqueMorseRepresentations(["a"]))