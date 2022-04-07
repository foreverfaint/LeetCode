from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = [n for n in nums if n % 2 == 1]
        evens = [n for n in nums if n % 2 == 0]
        ans = []
        for i,n in enumerate(odds):
            ans.append(evens[i])
            ans.append(n)
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.sortArrayByParityII([4,2,5,7]))
    print(sln.sortArrayByParityII([2,3]))