from typing import List
import random


class Solution:
    def partition(self, ans, low, high):
        # A random pivot is very important for efficiency. 
        # Otherwise if you use ans[low] or ans[high] as pivot, partition would be called in linear times when ans is inorder (asc or desc).
        ix = random.randint(low,high)
        ans[high], ans[ix] = ans[ix], ans[high]

        pivot = ans[high][1]
        i = low
        for j in range(low, high):
            if ans[j][1] < pivot:
                ans[j], ans[i] = ans[i], ans[j]
                i += 1
            j += 1

        ans[high], ans[i] = ans[i], ans[high]
        return i

    def find_kth_smallest(self, ans, k):
        low = 0
        high = len(ans) - 1
        while low < high:
            loc = self.partition(ans, low, high)
            if loc == k:
                return
            elif loc < k:
                low = loc + 1
            else:
                high = loc - 1

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points
        ans = [(p, p[0]**2 + p[1]**2) for p in points]
        self.find_kth_smallest(ans, k)
        return [x[0] for x in ans[:k]]


if __name__ == "__main__":
    sln = Solution()
    print(sln.kClosest([[1,3],[-2,2]], 1))
    print(sln.kClosest([[3,3],[5,-1],[-2,4]], 2))
    import cProfile
    cProfile.run("sln.kClosest([[x, -x] for x in range(10000)], 5000)")
    # print(sln.kClosest([[-2,5],[7,-2],[-8,0],[2,9],[-1,3],[-3,9],[-6,8],[-5,-5]], 7))
