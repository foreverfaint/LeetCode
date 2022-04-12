from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        start, destination = min(start, destination), max(start, destination)
        dist = sum([distance[i] for i in range(start, destination)])
        return min(dist, total - dist)


if __name__ == "__main__":
    sln = Solution()
    print(sln.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
    print(sln.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))
    print(sln.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))