from typing import List


class Solution:
    def find(self, nums, x):
        min_ = 0
        max_ = len(nums)
        while min_ < max_:
            mid = (min_ + max_) // 2
            if nums[mid] >= x:
                max_ = mid
            else:
                min_ = mid + 1
        return min_
            

    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_nums1 = sorted(nums1)
        max_s = 0
        max_i = -1
        for i, x in enumerate(nums2):
            origin = abs(nums1[i] - nums2[i])
            j = self.find(sorted_nums1, x)
            if j == 0:
                s = abs(sorted_nums1[j] - x)
            elif j == len(nums1):
                s = abs(sorted_nums1[j - 1] - x)
            else:
                s = min(abs(sorted_nums1[j] - x), abs(sorted_nums1[j - 1] - x))
            if origin - s > max_s:
                max_s = origin - s
                max_i = i
            print(f"i={i}, x={x}, sorted_nums2={sorted_nums1}, j={j}, s={s}, max_s={max_s}, max_i={max_i}")
        
        ans = sum([abs(n1 - n2) - max_s if i == max_i else abs(n1 - n2) for i, (n1, n2) in enumerate(zip(nums1, nums2))])
        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    sln = Solution()
    print(sln.minAbsoluteSumDiff(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]))
    print(sln.minAbsoluteSumDiff(nums1 = [1,7,5], nums2 = [2,3,5]))
    print(sln.minAbsoluteSumDiff(nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]))
