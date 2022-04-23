from typing import List


# class Solution:
#     def foo(self, nums, acc, k):
#         min_ = 0
#         max_ = len(acc) - 1
#         while min_ < max_:
#             mid = (min_ + max_) // 2
#             if nums[-1] * (len(nums) - mid) > k + (acc[-1] - (acc[mid - 1] if mid > 0 else 0)):
#                 min_ = mid + 1
#             else:
#                 max_ = mid            
#         return min_

#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums = sorted(nums)

#         acc = [0] * len(nums)
#         acc[0] = nums[0]
#         for i in range(1, len(nums)):
#             acc[i] = acc[i - 1] + nums[i]

#         ans = 0
#         for i in range(1, len(nums) + 1):
#             j = self.foo(nums[:i], acc[:i], k) 
#             f = i - j
#             ans = max(f, ans)
#             # print(nums[:i], f"j={j}, f={f}")
#         return ans


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:      
        nums = sorted(nums)
        i = 0
        s = 0
        ans = 0
        for j in range(len(nums)):
            s += nums[j]
            while nums[j] * (j - i + 1) > s + k:
                s -= nums[i]
                i += 1
            ans = max(ans, j - i + 1)
        return ans


if __name__ == "__main__":
    sln = Solution()
    
    print(sln.maxFrequency(nums = [1,2,4], k = 5)) # 3
    print(sln.maxFrequency(nums = [1,4,8,13], k = 5))     # 2
    print(sln.maxFrequency(nums = [3,9,6], k = 2))    # 1    
    print(sln.maxFrequency(nums = [9940,9995,9944,9937,9941,9952,9907,9952,9987,9964,9940,9914,9941,9933,9912,9934,9980,9907,9980,9944,9910,9997], k = 7925)) # 22
    print(sln.maxFrequency(nums = [9979,9938,9947,9916,9995,9981,9981,9931,9984,9942,9946,9946,9945,9931,9908,9920,9929,9917,9904,9945,9963,9910,9942,9965,9915,9981,9908,9919,9975,9904,9934,9922,9989,9946,9928,9928,9940,9941,9995,9905,9903,9980,9917,9940,9910,9994,9909,9965,9972,9931,9975,9913,9983,9943,9996,9917,9994,9991,9948,9961,9921,9981,9928,9933,9905,9957,9953,9940,9958,9982,9900,9912,9959,9992,9978,9988,9940,9985,9945,9900,9956,9976,9972,9914,9903,9978,9965,9987,9926,9963,9968,9962,9995,9963,9960,9986,9916,9911,9976,9988,9952,9914,9934,9929,9962,9999,9988,9901,9925,9983,9991,9915,9930,9949,9931,9944,9947,9921,9982,9984,9998,9945,9907,9900,9992,9945,9995,9941,9930,9918,9961,9960,9900,9952,9952,9954,9976,9970,9990,9947,9910,9908,9935,9971,9971,10000,9941,9983,9949,9985,9992,9996,9918,9930,9994,9970,9989,9975,9960,9973,9993,9900,9915,9974,9966,9978,9926,9937,9936,9952,9996,9996,9912,9915,9976,9976,9901,9926,9959,9989,9976,9904,9999,9925,9934,9947,9950,9985,9985,9932,9922,9962,9962,9993,9912,9924,9992,9941,9959,9954,9943,9995,9992,9928,9992,9920,9984,9917,9976,9971,9927,9917,9923,9948,9929,9990,9990,9921,9989,9910,9921], k = 2636)) 


    


    