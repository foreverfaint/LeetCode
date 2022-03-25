from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = 0
        ans = []
        while k > 0 or i >= 0:
            d1 = (k % 10) if k > 0 else 0
            d2 = num[i] if i >= 0 else 0
            s = d1 + d2 + carry
            # print(d1, d2, carry, s)
            if s < 10:
                ans.insert(0, s)
                carry = 0
            else:
                ans.insert(0, s - 10)
                carry = 1
            k = k // 10
            i -= 1

        if carry > 0:
            ans.insert(0, carry)
  
        return ans
        


if __name__ == "__main__":
    sln = Solution()
    print(sln.addToArrayForm([1,2,0,0], 34))
    print(sln.addToArrayForm([2,7,4], 181))
    print(sln.addToArrayForm([2,1,5], 806))