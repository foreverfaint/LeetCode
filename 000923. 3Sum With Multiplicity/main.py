from typing import List


class Solution:
    MAX = pow(10, 9) + 7


    def C(self, n, m):
        i = 1
        a = 1
        b = 1
        while i <= m:
            a *= n
            b *= i
            n -= 1
            i += 1
        return a // b

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        m = {}
        for n in arr:
            m.setdefault(n, 0)
            m[n] += 1

        ans = 0
        # C(cnt, 3) for any number which appears 3+ times in the original array. 
        for n, cnt in m.items():
            if cnt >= 3 and n * 3 == target:
                ans += self.C(cnt, 3)

        # C(cnt, 2) for 2 same numbers + 1 other number
        for n, cnt in m.items():
            n_k = target - 2 * n
            if cnt >= 2 and n_k != n and n_k in m:
                ans += self.C(cnt, 2) * m[n_k]

        # For 3 different numbers
        nums = list(m.keys())
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                n_i = nums[i]    
                n_j = nums[j]
                n_k = target - n_i - n_j
                if n_k in m and n_k > n_j and n_k > n_i:
                    ans += m[n_i] * m[n_j] * m[n_k]
        return ans % self.MAX

                

if __name__ == "__main__":
    sln = Solution()
    print(sln.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8))
    print(sln.threeSumMulti(arr = [1,1,2,2,2,2], target = 5))
    print(sln.threeSumMulti(arr = [0,0,0], target = 0))