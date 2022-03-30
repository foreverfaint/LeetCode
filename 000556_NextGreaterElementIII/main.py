from typing import List


class Solution:
    MAX = (1 << 31)

    def foo(self, n):
        nums = []
        while n > 0:
            nums.append(n % 10)
            n = n // 10
        nums.reverse()
        return nums


    def nextGreaterElement(self, n: int) -> int:
        nums = self.foo(n)
        
        i = len(nums) - 1
        while i >= 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i <= 0:
            return -1

        j = i
        while j < len(nums) and nums[i - 1] < nums[j]:
            j += 1

        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
        nums[i:] = nums[i:][::-1]
        n = int("".join([str(x) for x in nums]))
        return -1 if n >= self.MAX else n



if __name__ == "__main__":
    sln = Solution()
    print(sln.nextGreaterElement(12))
    print(sln.nextGreaterElement(21))
    print(sln.nextGreaterElement(51241))
    print(sln.nextGreaterElement(230241))
    print(sln.nextGreaterElement(2147483486), sln.MAX)
    print(sln.nextGreaterElement(2147483476), sln.MAX)



    # print(sln.gen(sln.foo(230241), 3, 4))