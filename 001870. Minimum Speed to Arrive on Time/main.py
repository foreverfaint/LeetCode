from typing import List


class Solution:
    def foo(self, dist, speed):
        import math
        return sum([math.ceil(d / speed) if i != len(dist) - 1 else d / speed for i, d in enumerate(dist)])

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        import math
        min_ = 1
        max_ = hour - math.floor(hour)
        max_ = math.ceil(max(dist) / max_) if max_ > 0 else (max(dist) + 1)
        while min_ < max_:
            speed = (min_ + max_) // 2
            time = self.foo(dist, speed)
            # print(f"min_={min_}, speed={speed}, max_={max_}, time={time}, hour={hour}")
            if time <= hour:
                max_ = speed
            else:
                min_ = speed + 1
        
        return -1 if self.foo(dist, min_) > hour else min_


if __name__ == "__main__":
    sln = Solution()
    print(sln.minSpeedOnTime(dist = [1,3,2], hour = 6))
    print(sln.minSpeedOnTime(dist = [1,3,2], hour = 2.7))
    print(sln.minSpeedOnTime(dist = [1,3,2], hour = 1.9))
    print(sln.minSpeedOnTime(dist = [1,1,100000], hour = 2.01))
    


