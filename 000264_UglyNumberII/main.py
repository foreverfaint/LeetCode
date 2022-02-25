from typing import List


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        # base case
        if n == 1:
            return 1
        
        # list containing all ugly numbers
        ugly = [1]
        
        # The pointers is to maintain the order of the ugly numbers
        p2, p3, p5 = 0, 0, 0
        
        i = 1
        while i < n:
            
            # An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
            a = ugly[p2] * 2
            b = ugly[p3] * 3
            c = ugly[p5] * 5
            
            # if we have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
            m = min(a, b, c)
            
            if a == m:
                p2 += 1            
            elif b == m:
                p3 += 1            
            else:
                p5 += 1
            
            # if repeat then no need to append into ugly just need to maintain pointer
            if m == ugly[-1]:                
                continue
                
            ugly.append(m)
            i += 1   
        return (ugly[-1])

    def nthUglyNumber2(self, n: int) -> int:
        if n == 1:
            return 1

        m = {1, 2, 3, 5}
        i = 2
        k = 1
        while True:
            if k == n:
                break

            for j in [2, 3, 5]:
                if i % j == 0:
                    t = i // j
                    if t in m:
                        k += 1
                        m.add(i)
                    break
            i += 1
        return i - 1
        


if __name__ == "__main__":
    sln = Solution()
    # print(sln.nthUglyNumber(1))
    # print(sln.nthUglyNumber(2))
    # print(sln.nthUglyNumber(3))
    # print(sln.nthUglyNumber(4))
    # print(sln.nthUglyNumber(5))
    # print(sln.nthUglyNumber(6))
    # print(sln.nthUglyNumber(7))
    # print(sln.nthUglyNumber(8))
    # print(sln.nthUglyNumber(9))
    # print(sln.nthUglyNumber(10))
    print(sln.nthUglyNumber(421))