from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        n = 0
        i = 1
        while True:
            if n + i > candies:
                ans[(i % num_people) - 1] += candies - n
                break
            n += i
            ans[(i % num_people) - 1] += i
            i += 1
        return ans
        


if __name__ == "__main__":
    sln = Solution()
    print(sln.distributeCandies(7, 4))
    print(sln.distributeCandies(10, 3))