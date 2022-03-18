from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
            
        ranges = [[nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] != ranges[-1][-1] + 1:
                ranges.append([])
            ranges[-1].append(nums[i])

        def _format(lst):
            if len(lst) == 1:
                return str(lst[0])
            return f"{lst[0]}->{lst[-1]}"

        return [_format(lst) for lst in ranges]


if __name__ == "__main__":
    sln = Solution()
    print(sln.summaryRanges([0,1,2,4,5,7]))
    print(sln.summaryRanges([0,2,3,4,6,8,9]))