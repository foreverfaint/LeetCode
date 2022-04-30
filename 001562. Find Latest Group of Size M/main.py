from tokenize import group
from typing import List


# Solution is right, but TLE
# class Solution:
#     def findLatestStep(self, arr: List[int], m: int) -> int:
#         n = len(arr)
#         if n == m:
#             return m

#         groups = [(1,n)]
#         print(groups)
#         for i in range(n - 1, -1, -1):
#             x = arr[i]
#             new_groups = None
#             for j, (start, end) in enumerate(groups):
#                 if start == x and end == x:
#                     new_groups = groups[:j] + groups[j + 1:]
#                     break
#                 elif end == x:
#                     new_groups = groups[:j] + groups[j + 1:] + [(start, end - 1)]
#                     break
#                 elif start == x:
#                     new_groups = groups[:j] + groups[j + 1:] + [(start + 1, end)]
#                     break
#                 elif start < x < end:
#                     new_groups = groups[:j] + groups[j + 1:] + [(start, x- 1), (x + 1, end)]
#                     break
#             groups = new_groups
#             print(groups)

#             if any([(end - start + 1) == m for start, end in groups]):
#                 return i
#         return -1


# Works, but still TLE
# class Solution:
#     def bs(self, x, groups):
#         low = 0
#         high = len(groups) - 1
#         while low < high:
#             mid = (low + high) // 2
#             start, end = groups[mid]
#             if start <= x and x <= end:
#                 return mid
#             elif x < start:
#                 high = mid
#             else:
#                 low = mid + 1
#         return low

#     def findLatestStep(self, arr: List[int], m: int) -> int:
#         n = len(arr)
#         if n == m:
#             return m

#         groups = [(1,n)]
#         print(groups)
#         for i in range(n - 1, -1, -1):
#             x = arr[i]
#             j =  self.bs(x, groups)
#             start, end = groups[j]
#             if start == x and end == x:
#                 groups = groups[:j] + groups[j + 1:]
#             elif end == x:
#                 groups = groups[:j] + [(start, end - 1)] + groups[j + 1:]
#             elif start == x:
#                 groups = groups[:j] + [(start + 1, end)] + groups[j + 1:]
#             elif start < x < end:
#                 groups = groups[:j] + [(start, x- 1), (x + 1, end)] + groups[j + 1:]
#             print(groups)

#             if any([(end - start + 1) == m for start, end in groups]):
#                 return i
#         return -1


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return m

        group_size = [0] * (n + 2)
        ans = -1
        for i in range(n):
            x = arr[i]
            left_group_size, right_group_size = group_size[x - 1], group_size[x + 1]
            if left_group_size == m or right_group_size == m:
                ans = i
            group_size[x - left_group_size] = group_size[x + right_group_size] = 1 + left_group_size + right_group_size
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.findLatestStep(arr = [1, 2], m = 1))  # 1
    print(sln.findLatestStep(arr = [1], m = 1))  # 1
    print(sln.findLatestStep(arr = [3,5,1,2,4], m = 1))  # 4
    print(sln.findLatestStep(arr = [3,1,5,4,2], m = 2)) # -1