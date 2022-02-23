class Solution:
    inf = pow(2, 31)
    pos_inf = inf - 1
    neg_inf = -inf

    def _crop(self, v):
        return min(max(v, self.neg_inf), self.pos_inf)

    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return self.pos_inf if dividend > 0 else -self.neg_inf

        if dividend == 0:
            return 0

        neg_flag = False
        if dividend < 0:
            dividend = -dividend
            neg_flag = True

        if divisor < 0:
            divisor = -divisor
            neg_flag = not neg_flag

        quotient = 0
        while dividend >= divisor:
            n = 1
            t = divisor
            while dividend >= t:
                t += t
                n += n
            
            quotient += (n >> 1)
            dividend -= (t >> 1)
        
        return self._crop(-quotient if neg_flag else quotient)


if __name__ == "__main__":
    sln = Solution()
    print(sln.divide(1, 1))
    print(sln.divide(5, 1))
    print(sln.divide(6, 2))
    print(sln.divide(10, 3))
    print(sln.divide(10, 0))
    print(sln.divide(0, 3))
    print(sln.divide(7, -3))
    print(sln.divide(-7, -3))
    print(sln.divide(-pow(2, 31) - 1, -1))
    print(sln.divide(pow(2, 31) - 1, 2))