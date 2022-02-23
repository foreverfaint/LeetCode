from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        i = 0
        prev_x = None
        while i < l:
            x = numbers[i]
            if x != prev_x:
                y = target - x
                j = i + 1
                while j < l:
                    if numbers[j] > y:
                        break
                    elif numbers[j] == y:
                        return [i + 1, j + 1]
                    j += 1
                prev_x = x
            i += 1


if __name__ == "__main__":
    sln = Solution()
    print(sln.twoSum([2,7,11,15], 9))
    print(sln.twoSum([2,3,4], 6))
    print(sln.twoSum([-1,0], -1))