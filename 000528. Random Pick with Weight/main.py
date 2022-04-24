from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.weights = [0] * len(w)
        self.weights[0] = w[0]
        for i in range(1, len(w)):
            self.weights[i] = self.weights[i - 1] + w[i]
        s = sum(w)
        self.weights = [n / s for n in self.weights]
        
    def pickIndex(self) -> int:
        import random
        r = random.random()
        for i, w in enumerate(self.weights):
            if r < w:
                return i
        return len(self.weights) - 1


if __name__ == "__main__":
    sln = Solution([1])
    print(sln.pickIndex())

    sln = Solution([1,3])
    print(sln.pickIndex())
    print(sln.pickIndex())
    print(sln.pickIndex())
    print(sln.pickIndex())
    print(sln.pickIndex())