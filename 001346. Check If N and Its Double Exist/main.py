from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zeros = len([n for n in arr if n == 0])
        if zeros > 1:
            return True

        target = set(arr)
        for n in arr:
            if n * 2 in target and n != 0:
                return True
        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.checkIfExist([-2,0,10,-19,4,6,-8]))
    print(sln.checkIfExist([10,2,5,3]))
    print(sln.checkIfExist([7,1,14,11]))
    print(sln.checkIfExist([3,1,7,11]))
    print(sln.checkIfExist([-2,0,10,-19,4,6,-8]))
    print(sln.checkIfExist([0, 0]))
    print(sln.checkIfExist([-20,8,-6,-14,0,-19,14,4]))
    
