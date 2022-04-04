from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        elif len(bits) == 2:
            return bits[0] == 0
        elif bits[0] == 0:
            return self.isOneBitCharacter(bits[1:])
        else:
            return self.isOneBitCharacter(bits[2:])



if __name__ == "__main__":
    sln = Solution()
    print(sln.isOneBitCharacter([1,0,0]))
    print(sln.isOneBitCharacter([1,1,1,0]))