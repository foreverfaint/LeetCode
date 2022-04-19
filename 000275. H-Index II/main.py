from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        min_ = 0
        max_ = max(max(citations), len(citations)) + 1
        ans = min_
        while min_ < max_:
            h = (min_ + max_) // 2
            actual_ = len([x for x in citations if x >= h])
            # print(f"min_={min_}, max_={max_}, h={h}, actual={actual_}")
            if actual_ < h:
                max_ = h
            else:
                if actual_ == h:
                    ans = max(ans, h)
                min_ = h + 1
        return min_ - 1


if __name__ == "__main__":
    sln = Solution()
    # 0
    print(sln.hIndex([0]))
    # 1
    print(sln.hIndex([1]))
    # 1
    print(sln.hIndex([100]))
    # 3
    print(sln.hIndex([0,1,3,5,6]))
    # 2
    print(sln.hIndex([1,2,100]))