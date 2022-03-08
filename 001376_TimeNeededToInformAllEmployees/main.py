from typing import List
from collections import defaultdict, deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append((i, informTime[manager[i]]))
            
        ret = 0
        queue = deque([(headID, 0)])
        while queue:
            cur_node, cur_t = queue.popleft()
            ret = max(ret, cur_t)
            for neighbor, dt in graph[cur_node]:
                queue.append((neighbor, cur_t+dt))
        return ret


if __name__ == "__main__":
    sln = Solution()
    sln.numOfMinutes(8, 0, [-1, 5, 0, 6, 7, 0, 0, 0], [89, 0, 0, 0, 0, 523, 241, 519])