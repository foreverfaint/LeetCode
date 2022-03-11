from typing import List


def gen_out_(edges):
    from collections import defaultdict

    out_ = defaultdict(list)
    for e in edges:
        out_[e[0]].append(e[1])
    return out_


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        sap = [-1] * n
        sap[0] = 0

        from queue import Queue

        q = Queue()

        out_ = [gen_out_(redEdges), gen_out_(blueEdges)]
        seen = [set(), set()]
        q.put_nowait((0, 0))
        while not q.empty():
            st, i = q.get_nowait()
            if st in seen[i % 2]:
                continue
            seen[i % 2].add(st)

            for ed in out_[i % 2][st]:
                sap[ed] = min(sap[ed], i + 1) if sap[ed] > -1 else (i + 1)
                q.put_nowait((ed, i + 1))

        out_.reverse()
        seen = [set(), set()]
        q.put_nowait((0, 0))
        while not q.empty():
            st, i = q.get_nowait()
            if st in seen[i % 2]:
                continue
            seen[i % 2].add(st)

            for ed in out_[i % 2][st]:
                sap[ed] = min(sap[ed], i + 1) if sap[ed] > -1 else (i + 1)
                q.put_nowait((ed, i + 1))

        return sap


if __name__ == "__main__":
    sln = Solution()
    print(sln.shortestAlternatingPaths(3, [[0, 1],[0,2]], [[1, 0]]))
    print(sln.shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]))
    print(sln.shortestAlternatingPaths(3, [[0, 1], [1, 2]], []))
    print(sln.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]]))
