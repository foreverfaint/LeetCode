from typing import List


class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.data = [[(self.snap_id, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        snap_list = self.data[index]
        snap_id, _ = snap_list[-1]
        if snap_id == self.snap_id:
            snap_list[-1] = (snap_id, val)
        else:
            snap_list.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_list = self.data[index]
        low = 0
        high = len(snap_list) - 1
        while low < high:
            mid = (low + high) // 2
            # print(f"low={low}, mid={mid}, high={high}, val={snap_list[mid]}, data={self.data}")
            if snap_list[mid][0] < snap_id:
                low = mid + 1
            else:
                high = mid
        return snap_list[low][1] if snap_list[low][0] <= snap_id else snap_list[low - 1][1]


if __name__ == "__main__":
    # sln.set(0, 5)
    # print(sln.snap())
    # sln.set(0, 6)
    # print(sln.get(0, 0))
    # print(sln.get(0, 1))

    # sln.set(1, 6)
    # print(sln.snap())
    # print(sln.snap())
    # sln.set(1, 19)
    # sln.set(0, 4)
    # print(sln.get(2, 1))
    # print(sln.get(2, 0))
    # print(sln.get(0, 1))

    sln = None
    res = []
    for i, (cmd, args) in enumerate(zip(
        ["SnapshotArray","set","snap","set","get"],
        [[3],[0,5],[],[0,6],[0,0]]
    )):
        if i == 0:
            sln = SnapshotArray(*args)
            res.append(None)
        else:
            res.append(eval(f"sln.{cmd}(*{args})"))
    # [null,null,0,null,5]
    print(res)
