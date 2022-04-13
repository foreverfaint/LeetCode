from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_m = {}
        min_v = float("inf")
        for i in range(1, len(arr)):
            a = arr[i - 1]
            b = arr[i]
            if b - a < min_v:
                min_v = b - a
            min_m.setdefault(b - a, [])
            min_m[b - a].append((a, b))
        return min_m[min_v]


if __name__ == "__main__":
    sln = Solution()
    print(sln.minimumAbsDifference([4,2,1,3]))
    print(sln.minimumAbsDifference([1,3,6,10,15]))
    print(sln.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))