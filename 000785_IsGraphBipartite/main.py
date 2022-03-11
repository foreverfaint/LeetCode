from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        from queue import Queue
        q = Queue()

        for i in range(len(graph)):
            if color[i] != 0:
                continue

            color[i] = 1
            q.put_nowait(i)

            while not q.empty():
                st = q.get_nowait()
                for ed in graph[st]:
                    ed_color = 2 if color[st] == 1 else 1
                    if color[ed] == 0:
                        color[ed] = ed_color
                        q.put_nowait(ed)
                    elif color[ed] != ed_color:
                        return False

        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
    print(sln.isBipartite([[1,3],[0,2],[1,3],[0,2]]))