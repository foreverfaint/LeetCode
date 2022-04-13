from typing import List


class Solution:
    def cmp(self, arr, i, j):
        loc_i, val_i, _ = arr[i]
        loc_j, val_j, _ = arr[j]
        return loc_i - loc_j  if val_i == val_j else val_i - val_j

    def partition(self, arr, low, high):
        if low >= high:
            return 0

        # A random pivot is very important for efficiency. 
        # Otherwise if you use ans[low] or ans[high] as pivot, partition would be called in linear times when ans is inorder (asc or desc).
        import random
        pivot = random.randint(low, high)
        arr[pivot], arr[high] = arr[high], arr[pivot]

        pivot_loc = low
        while low < high:
            if self.cmp(arr, low, high) < 0:
                arr[low], arr[pivot_loc] = arr[pivot_loc], arr[low]
                pivot_loc += 1
            low += 1

        arr[high], arr[pivot_loc] = arr[pivot_loc], arr[high]
        return pivot_loc

    def sort(self, arr: List[int], low, high, k: int):
        if low >= high:
            return

        pivot_loc = self.partition(arr, low, high)
        if pivot_loc == k:
            return
        elif pivot_loc < k:
            low = self.sort(arr, pivot_loc + 1, high, k)
        else:
            low = self.sort(arr, low, pivot_loc - 1, k)


    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        arr = [(i, abs(n - x), n) for i, n in enumerate(arr)]
        self.sort(arr, 0, len(arr) - 1, k)
        return sorted([n for _, _, n in arr[:k]])



if __name__ == "__main__":
    sln = Solution()
    print(sln.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
    print(sln.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1))
    print(sln.findClosestElements(arr = [-2,-1,1,2,3,4,5], k = 7, x = 3))
    print(sln.findClosestElements(arr = [0,1,2,2,2,3,6,8,8,9], k = 5, x = 9))
