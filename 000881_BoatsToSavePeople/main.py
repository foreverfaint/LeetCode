from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        n = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if i == j:
                # print("-", people[j])
                n += 1
                break
            if people[j] == limit:
                # print("-", people[j])
                j -= 1
                n += 1
            elif people[i] + people[j] > limit:
                # print("-", people[j])
                j -= 1
                n += 1
            else:
                # print("-", people[j], people[i])
                j -= 1
                i += 1
                n += 1
        return n
        

if __name__ == "__main__":
    sln = Solution()
    print(sln.numRescueBoats([1,2], 3))
    print(sln.numRescueBoats([3,2,2,1], 3))
    print(sln.numRescueBoats([3,5,3,4], 5))