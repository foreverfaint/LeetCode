from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            m.setdefault(n,0)
            m[n] += 1

        m = list(m.items())
        for i in range(k):
            for j in range(i + 1, len(m)):
                if m[j][1] > m[i][1]:
                    m[i], m[j] = m[j], m[i]
        return [x[0] for x in m[:k]]


if __name__ == "__main__":
    sln = Solution()
    print(sln.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(sln.topKFrequent([1], 1))
