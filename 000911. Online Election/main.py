from typing import List


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.winner = []
        self.times = times
        votes = {}
        for i, person in enumerate(persons):
            votes.setdefault(person, 0)
            votes[person] += 1
            if not self.winner:
                self.winner.append(person)
            else:
                if votes[self.winner[-1]] > votes[person]:
                    self.winner.append(self.winner[-1])
                else:
                    self.winner.append(person)

    def q(self, t: int) -> int:
        if t >= self.times[-1]:
            return self.winner[-1]

        low = 0
        high = len(self.times)
        while low < high:
            mid = (low + high) // 2
            if self.times[mid] < t:
                low = mid + 1
            else:
                high = mid

        i = low if self.times[low] <= t else low - 1
        return self.winner[i]


if __name__ == "__main__":
    sln = None
    res = []
    for i, (cmd, args) in enumerate(zip(
# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"],
# [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
        ["TopVotedCandidate","q","q","q","q","q","q","q","q","q","q"],
        [[[0,0,0,0,1],[0,6,39,52,75]],[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]]
    )):
        if i == 0:
            sln = TopVotedCandidate(*args)
            print(sln.winner, *args)
            res.append(None)
        else:
            res.append(eval(f"sln.{cmd}(*{args})"))
            print(f"sln.{cmd}(*{args})",  "=>", res[-1])
    print(res)