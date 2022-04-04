from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        m5 = 0
        m10 = 0
        for bill in bills:
            if bill == 5:
                m5 += 1
            elif bill == 10:
                if m5 > 0:
                    m5 -= 1
                    m10 += 1
                else:
                    return False
            else:
                if m10 > 0:
                    if m5 > 0:
                        m10 -= 1
                        m5 -= 1
                    else:
                        return False
                elif m5 >= 3:
                    m5 -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.lemonadeChange([5,5,5,10,20]))
    print(sln.lemonadeChange([5,5,10,10,20]))