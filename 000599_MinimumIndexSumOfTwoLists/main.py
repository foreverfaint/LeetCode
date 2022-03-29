from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m1 = {s: i for i, s in enumerate(list1)}
        m2 = {s: i for i, s in enumerate(list2)}
        ans = []
        min_ = None
        for s, i in m1.items():
            j = m2.get(s)
            if j is not None:
                if min_ is None:
                    min_ = i + j
                    ans = [s]
                elif i + j < min_:
                    min_ = i + j
                    ans = [s]
                elif i + j == min_:
                    ans.append(s)
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))
    print(sln.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
    print(sln.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))