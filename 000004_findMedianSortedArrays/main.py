from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        loc = 0
        mean = 0
        n = len(nums1)
        m = len(nums2)
        loc_1 = (n + m - 1) // 2
        loc_2 = (n + m) // 2
    
        while i < n or j < m:
            if i < n and j < m:
                if nums1[i] < nums2[j]:
                    num = nums1[i]
                    i += 1
                else:
                    num = nums2[j]
                    j += 1
            elif i < n:
                num = nums1[i]
                i += 1
            else:
                num = nums2[j]
                j += 1
            

            if loc == loc_1:
                mean += num
            
            if loc == loc_2:
                mean += num
                return mean / 2

            loc += 1


def assert_float_0(expected: float, actual: float) -> bool:
    print(f"expected={expected}, actual={actual}")
    return abs(expected - actual) < 1e-6


if __name__ == "__main__":
    assert_float_0(2.00000, Solution().findMedianSortedArrays([1,3], [2]))
    assert_float_0(2.50000, Solution().findMedianSortedArrays([1,2], [3,4]))