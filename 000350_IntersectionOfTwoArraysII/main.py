from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1 = {}
        for x in nums1:
            m1.setdefault(x, 0)
            m1[x] += 1

        m2 = {}
        for x in nums2:
            m2.setdefault(x, 0)
            m2[x] += 1

        r = []
        for x, t1 in m1.items():
            t2 = m2.get(x)
            if t2:
                for _ in range(min(t1, t2)):
                    r.append(x)

        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.intersect([1,2,2,1], [2,2]))
    print(sln.intersect([4,9,5], [9,4,9,8,4]))