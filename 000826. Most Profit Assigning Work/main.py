from typing import List


class Solution:
    def bs(self, nums, low, high, target):
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return -1 if nums[low] < target else low
            

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker = sorted(worker)
        pairs = sorted(list(zip(difficulty, profit)), key=lambda p: p[1], reverse=True)
        low = 0
        high = len(worker) - 1
        ans = 0
        for p in pairs:
            difficulty, profit = p
            i = self.bs(worker, low, high, difficulty)
            if i > -1:
                ans += (high - i + 1) * profit
                high = i - 1
        return ans


if __name__ == "__main__":
    sln = Solution()
    # print(sln.bs([4,5,6,7], 0, 3, 10))
    # print(sln.bs([4,5,6,7], 0, 3, 8))
    # print(sln.bs([4,5,6,7], 0, 3, 6))
    # print(sln.bs([4,5,6,7], 0, 1, 4))
    print(sln.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))
    print(sln.maxProfitAssignment(difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]))
    print(sln.maxProfitAssignment(difficulty = [13,37,58], profit = [4,90,96], worker = [34,73,45]))

