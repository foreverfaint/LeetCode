from typing import List


def decode(str) -> List[int]:
    return [int(x) for x in str]


def encode(arr) -> str:
    return "".join([str(x) for x in arr])


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        from queue import Queue
        q = Queue()
        q.put_nowait(("0000", 0))

        seen = set()
        while not q.empty():
            turn, turns = q.get_nowait()

            if turn in seen:
                continue
            seen.add(turn)

            if turn in deadends:
                continue

            if turn == target:
                return turns

            turn = decode(turn)
            for i in range(4):
                for d in [-1, 1]:
                    new_turn = list(turn)
                    new_turn[i] = (new_turn[i] + d) % 10
                    q.put_nowait((encode(new_turn), turns + 1))

        return -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
    print(sln.openLock(["8888"], "0009"))
    print(
        sln.openLock(
            ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
        )
    )
