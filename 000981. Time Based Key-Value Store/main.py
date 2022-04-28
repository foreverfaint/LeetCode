from typing import List


class TimeMap:
    def __init__(self):
        self.m = {}

    def bs(self, arr, target):
        low = 0
        high = len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid][0] < target:
                low = mid + 1
            else:
                high = mid
        return low
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m.setdefault(key, [])
        lst: List = self.m[key]
        p = self.bs(lst, timestamp)
        lst.insert(p, (timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.m.get(key)
        if not lst:
            return ""

        p = self.bs(lst, timestamp)
        if p >= len(lst):
            return lst[-1][1]
        elif timestamp == lst[p][0]:
            return lst[p][1]
        elif p == 0:
            return ""
        else:
            return lst[p-1][1]


if __name__ == "__main__":
    sln = TimeMap()
    # sln.set("foo", "bar", 1)
    # print(sln.get("foo", 1))
    # print(sln.get("foo", 3))
    # sln.set("foo", "bar2", 4)
    # print(sln.get("foo", 4))
    # print(sln.get("foo", 5))

    actual = []

    sln: TimeMap = None
    for cmd, args in zip(
        ["TimeMap","set","set","get","get","get","get","get"],
        [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
    ):
        if cmd == "TimeMap":
            sln = TimeMap()
            actual.append("null")
        elif cmd == "set":
            sln.set(*args)
            actual.append("null")
        else:
            actual.append(sln.get(*args))

    print(actual)
    print(["null","null","null","","high","high","low","low"])