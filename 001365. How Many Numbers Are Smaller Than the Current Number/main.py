from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        from collections import Counter
        ans = {}
        acc = 0
        for n, f in sorted(Counter(nums).most_common(), key=lambda kv: kv[0]):
            ans[n] = acc
            acc += f
        return [ans.get(n) for n in nums]    


if __name__ == "__main__":
    sln = Solution()
    print(sln.smallerNumbersThanCurrent([8,1,2,2,3]))
    print(sln.smallerNumbersThanCurrent([6,5,4,8]))
    print(sln.smallerNumbersThanCurrent([7,7,7,7]))