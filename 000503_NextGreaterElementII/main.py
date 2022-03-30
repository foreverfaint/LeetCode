from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        ans = [-1] * len(nums)
        from collections import deque
        stack = deque()
        for i in range(len(nums)):
            while len(stack) > 0 and stack[-1][0] < nums[i]:
                top = stack.pop()
                ans[top[1]] = nums[i]
            stack.append((nums[i], i))

        for i in range(len(nums)):
            while len(stack) > 0 and stack[-1][0] < nums[i]:
                top = stack.pop()
                ans[top[1]] = nums[i]

        return ans



if __name__ == "__main__":
    sln = Solution()
    print(sln.nextGreaterElements([1,2,1]))
    print(sln.nextGreaterElements([1,2,3,4,3]))