from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        i = m - 1
        while i >= 0:
            nums1[i + n] = nums1[i]
            i -= 1

        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i + n] < nums2[j]:
                nums1[k] = nums1[i + n]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            nums1[k] = nums1[i + n]
            i += 1
            k += 1

        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1



if __name__ == "__main__":
    sln = Solution()

    # nums1 = [1,2,3,0,0,0]
    # nums2 = [2,5,6]
    # sln.merge(nums1, 3, nums2, 3)
    # print(nums1)

    # nums1 = [1]
    # nums2 = []
    # sln.merge(nums1, 1, nums2, 0)
    # print(nums1)

    # nums1 = [0]
    # nums2 = [1]
    # sln.merge(nums1, 0, nums2, 1)
    # print(nums1)

    nums1 = [1,2,4,5,6,0]
    nums2 = [3]
    sln.merge(nums1, 5, nums2, 1)
    print(nums1)
        