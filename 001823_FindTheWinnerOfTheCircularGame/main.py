from typing import List


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        from collections import deque
        q = deque()
        for i in range(1, n + 1):
            q.append(i)

        i = 0
        while len(q) > 1:
            friend = q.popleft()
            if i % k != k - 1:
                q.append(friend)
            i += 1

        return q.pop()


if __name__ == "__main__":
    sln = Solution()
    print(sln.findTheWinner(5, 2))
    print(sln.findTheWinner(6, 5))