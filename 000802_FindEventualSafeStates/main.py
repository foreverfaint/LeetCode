from typing import List


def dfs(st: int, graph, state, path) -> bool:
    if state[st] > 0:
        return state[st] == 1

    state[st] = 2
    for st_ in graph[st]:
        if not dfs(st_, graph, state, path):
            return False
    state[st] = 1
    return True



class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = set()
        state = [0] * len(graph)
        for i in range(len(graph)):
            if dfs(i, graph, state, set()):
                safe.add(i)
        return sorted(list(safe))


if __name__ == "__main__":
    sln = Solution()
    print(sln.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
    print(sln.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
