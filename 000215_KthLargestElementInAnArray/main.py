from typing import List


class Solution:
    def partition(self, ans, ngt, low, high):
        if low >= high:
            return 0

        loc = low
        while low < high:
            if ngt(ans[low], ans[high]):
                ans[low], ans[loc] = ans[loc], ans[low]
                loc += 1
            low += 1
        ans[high], ans[loc] = ans[loc], ans[high]
        return loc

    def find_kth_smallest(self, ans, ngt, low, high, k):
        if low >= high:
            return

        loc = self.partition(ans, ngt, low, high)
        if loc + 1 < k:
            self.find_kth_smallest(ans, ngt, loc + 1, high, k)
        elif loc + 1 > k:
            self.find_kth_smallest(ans, ngt, low, loc - 1, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        self.find_kth_smallest(nums, lambda x, y: x <= y, 0, len(nums) - 1, k)
        nums = [-x for x in nums]
        return nums[k - 1]


if __name__ == "__main__":
    sln = Solution()
    print(sln.findKthLargest([3,2,1,5,6,4], 2))
    print(sln.findKthLargest([3,2,3,1,2,4,5,5,6], 4))