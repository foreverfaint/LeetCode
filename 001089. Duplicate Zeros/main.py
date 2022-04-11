from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        l = len(arr)
        while i < l:
            if arr[i] == 0 and i + 1 < l:
                j = l - 2
                while j > i:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[i + 1] = 0
                i += 1
            i += 1


if __name__ == "__main__":
    sln = Solution()
    
    arr = [1,0,2,3,0,4,5,0]
    sln.duplicateZeros(arr)
    print(arr)
    
    arr = [1,2,3]
    sln.duplicateZeros(arr)
    print(arr)