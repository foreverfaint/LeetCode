from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if target < c:
                return c
        return letters[0]


if __name__ == "__main__":
    sln = Solution()
    print(sln.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
    print(sln.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
    print(sln.nextGreatestLetter(letters = ["c","f","j"], target = "d"))
    print(sln.nextGreatestLetter(letters = ['a', 'b'], target = 'z'))