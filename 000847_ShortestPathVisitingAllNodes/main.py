from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        from queue import Queue
        q = Queue()
        for i in range(len(graph)):
            q.put_nowait((i, 1 << i, 0))

        target = (1 << len(graph)) - 1

        seen = set()
        while not q.empty():
            st, state, cnt = q.get_nowait()
            print(st, state, cnt)
            
            if (st, state) in seen:
                continue
            seen.add((st, state))

            if state == target:
                return cnt

            for ed in graph[st]:
                q.put_nowait((ed, state | (1 << ed), cnt + 1))

        return -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.shortestPathLength([[1, 2, 3], [0], [0], [0]]))
    print(sln.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
