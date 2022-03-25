from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = sum([x[0] for x in costs])
        refund = sorted([x[1] - x[0] for x in costs])
        print(refund)
        return cost + sum(refund[:len(costs) // 2])



if __name__ == "__main__":
    sln = Solution()
    print(sln.twoCitySchedCost([[70,311],[74,927],[732,711],[126,583],[857,118],[97,928],[975,843],[175,221],[284,929],[816,602],[689,863],[721,888]]))

    print(sln.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
    print(sln.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
    print(sln.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))
    