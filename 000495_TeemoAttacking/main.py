from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        d = 0
        end = -1
        for start in timeSeries:
            new_end = start + duration - 1
            if start > end:
                d += duration
                end = new_end
            elif new_end <= end:
                continue
            else:
                d += new_end - end
                end = new_end
        return d


if __name__ == "__main__":
    sln = Solution()
    print(sln.findPoisonedDuration([1,4], 2))
    print(sln.findPoisonedDuration([1,2], 2))