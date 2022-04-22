from typing import List


class Solution:
    def bs(self, starts, end):
        low = 0
        high = len(starts) - 1
        while low < high:
            mid = (low + high) // 2
            if starts[mid][0] < end:
                low = mid + 1
            else:
                high = mid
        # print(starts, starts[low][0], end, "->", starts[low][1])
        return -1 if starts[low][0] < end else starts[low][1]

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted([(interval[0], i) for i, interval in enumerate(intervals)], key=lambda p: p[0])
        return [self.bs(starts, interval[1]) for interval in intervals]


if __name__ == "__main__":
    sln = Solution()
    print(sln.findRightInterval([[1,2]]))
    print(sln.findRightInterval([[3,4],[2,3],[1,2]]))
    print(sln.findRightInterval([[1,4],[2,3],[3,4]]))