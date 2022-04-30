
class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        j = 0
        for i, (start_, end_) in enumerate(self.events):
            if start_ <= start < end_ or start_ < end <= end_:
                return False
            if start <= start_ < end or start < end_ <= end:
                return False
            elif start < start_:
                break
            j += 1

        self.events.insert(j, (start, end))
        return True


if __name__ == "__main__":
    print(sorted([(1, 2), (2, 3), (2, 1)]))

    sln = None
    res = []
    for i, (cmd, args) in enumerate(zip(
# ["MyCalendar", "book", "book", "book"],
# [[], [10, 20], [15, 25], [20, 30]]
["MyCalendar","book","book","book","book","book","book","book","book","book","book"],
[[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
    )):
        if i == 0:
            sln = MyCalendar(*args)
            res.append(None)
        else:
            res.append(eval(f"sln.{cmd}(*{args})"))
            print(args, sln.events)
    print(res)