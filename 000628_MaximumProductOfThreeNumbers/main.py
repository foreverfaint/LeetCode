from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pos = sorted([n for n in nums if n > 0])
        neg = sorted([n for n in nums if n < 0])
        
        cands = [0] if 0 in nums else []
        if len(pos) >= 3:
            cands.append(pos[-1] * pos[-2] * pos[-3]) # +
        if len(pos) >= 2 and len(neg) >= 1:
            cands.append(pos[0] * pos[1] * neg[-1]) # -
        if len(pos) >= 1 and len(neg) >= 2:
            cands.append(pos[-1] * neg[0] * neg[1]) # +
        if len(neg) >= 3:
            cands.append(neg[-1] * neg[-2] * neg[-3]) # -
        return max(cands)




if __name__ == "__main__":
    sln = Solution()
    print(sln.maximumProduct([1,2,3]))
    print(sln.maximumProduct([1,2,3,4]))
    print(sln.maximumProduct([-1,-2,-3]))
    print(sln.maximumProduct([-100,-98,-1,2,3,4]))
    print(sln.maximumProduct([-100,-2,-3,1]))
    print(sln.maximumProduct([-8,-7,-2,10,20]))