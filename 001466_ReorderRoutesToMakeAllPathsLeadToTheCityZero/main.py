from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        from collections import defaultdict
        in_ = defaultdict(list)
        out = defaultdict(list)
        for e in connections:
            in_[e[1]].append(e[0])
            out[e[0]].append(e[1])

        c = 0
        connected = set()
        from queue import Queue
        q = Queue()
        q.put_nowait(0)
        while not q.empty():
            sn = q.get_nowait()
            connected.add(sn)

            for n in in_[sn]:
                if n not in connected:
                    q.put_nowait(n)

            for n in out[sn]:
                if n not in connected:
                    c += 1
                    q.put_nowait(n)

        return c


if __name__ == "__main__":
    sln = Solution()
    # 3
    print(sln.minReorder(7, [[0,6],[6,3],[1,3],[2,1],[4,0],[4,5]]))
    # 1
    print(sln.minReorder(4, [[0,1],[2,0],[3,2]]))
    # 3
    print(sln.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
    # 2
    print(sln.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
    # 0
    print(sln.minReorder(3, [[1, 0], [2, 0]]))
