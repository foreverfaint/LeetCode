from typing import List


class Solution:
    def findLeftNonDescSubarray(self, arr):
        i = 0
        while i < len(arr) - 1:
            if arr[i] > arr[i + 1]:
                break
            i += 1
        return arr[:i+1]

    def findRightNonDescSubarray(self, arr):
        i = len(arr) - 1
        while i > 0:
            if arr[i] < arr[i - 1]:
                break
            i -= 1
        return arr[i:]

    def bs(self, arr, target):
        low = 0
        high = len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = len(arr)
        left_subarr = self.findLeftNonDescSubarray(arr)
        l_l = len(left_subarr)
        if l == l_l:
            return 0
        
        right_subarr = self.findRightNonDescSubarray(arr)
        r_l = len(right_subarr)
        if l == r_l:
            return 0

        ans = min(l - r_l, l - l_l)
        for i, n in enumerate(left_subarr):
            j = self.bs(right_subarr, n)
            if j != r_l:
                l_desc_len = i + 1
                r_desc_len = max(0, r_l - j)
                desc_len = l_desc_len + r_desc_len
                ans = min(ans, l - desc_len)
        return ans
            


if __name__ == "__main__":
    sln = Solution()
    # print(sln.findLeftNonDescSubarray([1,2,3,10,4,2,3,5]))
    # print(sln.findRightNonDescSubarray([1,2,3,10,4,2,3,5]))
    # print(sln.bs([2,3,5], 1))
    # print(sln.bs([2,3,5], 2))
    # print(sln.bs([2,3,5], 3))
    # print(sln.bs([2,3,5], 10))

    print(sln.findLengthOfShortestSubarray([16,10,0,3,22,1,14,7,1,12,15]))
    print(sln.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))
    print(sln.findLengthOfShortestSubarray([5,4,3,2,1]))
    print(sln.findLengthOfShortestSubarray([1,2,3]))
