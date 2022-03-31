from typing import List


class Solution:
    def split(self, nums, largest):
        s = 0
        m = 0
        for n in nums:
            s += n
            if s > largest:
                m += 1
                s = n
        return m + 1

    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        r = sum(nums)
        # print('min=', l, 'max=', r)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            groups = self.split(nums, mid)
            # print('l=', l, 'r=', r, 'largest=', mid, 'groups=', groups, 'ans=', ans)
            if groups <= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans



if __name__ == "__main__":
    sln = Solution()

    print(sln.splitArray(nums = [7,2,5,10,8], m = 2))
    print(sln.splitArray(nums = [1,2,3,4,5], m = 2))
    print(sln.splitArray(nums = [1,4,4], m = 3))