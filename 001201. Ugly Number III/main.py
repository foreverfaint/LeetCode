from typing import List


# Work but TLE
# class Solution:
#     def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
#         dup = set([a, b, c])
#         import heapq
#         arr = [(x, x, 1) for x in [a, b, c]]
#         heapq.heapify(arr)
#         i = 0
#         while True:
#             i += 1
#             e1 = heapq.heappop(arr)
#             k, x, multi = e1
#             print(f"i={i}, k={k} ~ {x} * {multi}")
#             if i == n:
#                 return k

#             if i == 10:
#                 break
            
#             multi += 1
#             new_k = x * multi
#             if new_k not in dup:
#                 heapq.heappush(arr, (new_k, x, multi))
#                 dup.add(new_k)


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def enough(num) -> bool:
            total = mid//a + mid//b + mid//c - mid//ab - mid//ac - mid//bc + mid//abc
            return total >= n

        import math
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = a * bc // math.gcd(a, bc)
        left, right = 1, 10 ** 10
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    sln = Solution()

    # print(sln.nthUglyNumber(n = 1000000000, a = 2, b = 217983653, c = 336916467))
    print(sln.nthUglyNumber(n = 3, a = 2, b = 3, c = 5))
    print(sln.nthUglyNumber(n = 4, a = 2, b = 3, c = 4))
    print(sln.nthUglyNumber(n = 5, a = 2, b = 11, c = 13))