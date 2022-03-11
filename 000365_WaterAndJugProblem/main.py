from typing import List


def _print(*args):
    #print(*args)
    pass


class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        from queue import Queue
        q = Queue()
        q.put_nowait(0)

        seen = set()
        seen.add(0)
        while not q.empty():
            total = q.get_nowait()

            if total == targetCapacity:
                return True

            for change in [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]:
                new_total = total + change
                if 0 < new_total and new_total <= jug1Capacity + jug2Capacity and new_total not in seen:
                    _print("-", total, "->", new_total)
                    seen.add(new_total)
                    q.put_nowait(new_total)

        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.canMeasureWater(104597, 104623, 123))
    print(sln.canMeasureWater(3, 5, 4))
    print(sln.canMeasureWater(2, 6, 5))
    print(sln.canMeasureWater(1, 2, 3))
