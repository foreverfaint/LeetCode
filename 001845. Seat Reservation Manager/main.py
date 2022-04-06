from typing import List


class SeatManager:
    def __init__(self, n: int):
        import heapq
        self.availabe_seats = [x + 1 for x in range(n)]
        heapq.heapify(self.availabe_seats)
        self.reserved_seats = set()

    def reserve(self) -> int:
        import heapq
        small = heapq.heappop(self.availabe_seats)
        self.reserved_seats.add(small)
        return small
        
    def unreserve(self, seatNumber: int) -> None:
        if seatNumber in self.reserved_seats:
            self.reserved_seats.remove(seatNumber)
            import heapq
            heapq.heappush(self.availabe_seats, seatNumber)


if __name__ == "__main__":
    sln = SeatManager(5)
    print(sln.reserve())
    print(sln.reserve())
    print(sln.unreserve(2))
    print(sln.reserve())
    print(sln.reserve())
    print(sln.reserve())
    print(sln.reserve())
    print(sln.unreserve(5))