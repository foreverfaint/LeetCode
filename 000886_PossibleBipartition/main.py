from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [0] * n

        from collections import defaultdict
        graph = defaultdict(list)
        for dislike in dislikes:
            i = dislike[0] - 1
            j = dislike[1] - 1
            graph[i].append(j)
            graph[j].append(i)

        from queue import Queue
        q = Queue()
        for i in list(graph.keys()):
            if color[i] != 0:
                continue

            color[i] = 1
            q.put_nowait(i)

            while not q.empty():
                st = q.get_nowait()
                ed_list = graph[st]
                for ed in ed_list:
                    ed_color = 2 if color[st] == 1 else 1
                    if color[ed] == 0:
                        color[ed] = ed_color
                        q.put_nowait(ed)
                    elif color[ed] != ed_color:
                        return False

        return True        


if __name__ == "__main__":
    sln = Solution()
    print(sln.possibleBipartition(10, [[5,9],[5,10],[5,6],[5,7],[1,5],[4,5],[2,5],[5,8],[3,5]]))
    print(sln.possibleBipartition(4, [[1,2],[1,3],[2,4]]))
    print(sln.possibleBipartition(3, [[1,2],[1,3],[2,3]]))
    print(sln.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))