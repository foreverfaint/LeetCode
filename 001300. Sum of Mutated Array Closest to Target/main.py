from typing import List
import math


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)
        l = len(arr)

        closest_abs_diff = float("inf")
        closest_v = None
        
        presum = 0
        for i in range(l):
            n = l - i
            v = (target - presum) / (l - i)

            low_v = math.floor(v) 
            if (i == 0 and low_v <= arr[0]) or (arr[i - 1] < low_v <= arr[i]):
                abs_diff = abs(target - (presum + low_v * n))
                if abs_diff < closest_abs_diff:
                    closest_abs_diff = abs_diff
                    closest_v = low_v
            
            high_v = math.ceil(v)
            if (i == 0 and high_v <= arr[0]) or (arr[i - 1] < high_v <= arr[i]):
                abs_diff = abs(target - (presum + high_v * n))
                if abs_diff < closest_abs_diff:
                    closest_abs_diff = abs_diff
                    closest_v = high_v

            presum += arr[i]

        if abs(target - presum) < closest_abs_diff:
            closest_v = arr[-1]

        return closest_v



if __name__ == "__main__":
    sln = Solution()
    print(sln.findBestValue(arr = [4,9,3], target = 10))
    print(sln.findBestValue(arr = [2,3,5], target = 10))
    print(sln.findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803))