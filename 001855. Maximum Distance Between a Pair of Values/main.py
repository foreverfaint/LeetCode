from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        i = 0
        l1 = len(nums1)
        j = 1
        l2 = len(nums2)
        while i + ans < l2 and i < l1 and j < l2:
            if nums2[j] >= nums1[i]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
                j = max(i + 1, j)
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))
    print(sln.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))
    print(sln.maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]))

    