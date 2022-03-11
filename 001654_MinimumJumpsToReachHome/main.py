from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)

        upper_bound = max(x, max(forbidden)) + a + b

        from queue import Queue

        q = Queue()
        q.put_nowait((0, True, 0))
        
        seen = set()
        # each position takes 2 slots of seen:
        # pos + forward
        # pos + backward
        # so when a pos is reached with forward flag, then we allow this pos could be reached again with backward flag
        seen.add((True, 0))
        while not q.empty():
            loc, can_backward, times = q.get_nowait()

            if loc == x:
                return times

            new_loc = loc + a
            if new_loc <= upper_bound and (True, new_loc) not in seen and new_loc not in forbidden:
                seen.add((True, new_loc))
                q.put_nowait((loc + a, True, times + 1))

            new_loc = loc - b
            if can_backward and new_loc >= 0 and (False, new_loc) not in seen and new_loc not in forbidden:
                seen.add((False, new_loc))
                q.put_nowait((loc - b, False, times + 1))

        return -1

# from collections import deque

# class Solution:
#     def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
#         dq, seen, steps, furthest = (
#             deque([(True, 0)]),
#             {(True, 0)},
#             0,
#             max(x, max(forbidden)) + a + b,
#         )
#         for pos in forbidden:
#             seen.add((True, pos))
#             seen.add((False, pos))
#         while dq:
#             for _ in range(len(dq)):
#                 dir, pos = dq.popleft()
#                 print(pos, x, False if dir else True, steps)
#                 if pos == x:
#                     return steps
#                 forward, backward = (True, pos + a), (False, pos - b)
#                 if pos + a <= furthest and forward not in seen:
#                     seen.add(forward)
#                     dq.append(forward)
#                 if dir and pos - b > 0 and backward not in seen:
#                     seen.add(backward)
#                     dq.append(backward)
#             steps += 1
#         return -1


if __name__ == "__main__":
    sln = Solution()
    print(
        sln.minimumJumps(
            [
                162,
                118,
                178,
                152,
                167,
                100,
                40,
                74,
                199,
                186,
                26,
                73,
                200,
                127,
                30,
                124,
                193,
                84,
                184,
                36,
                103,
                149,
                153,
                9,
                54,
                154,
                133,
                95,
                45,
                198,
                79,
                157,
                64,
                122,
                59,
                71,
                48,
                177,
                82,
                35,
                14,
                176,
                16,
                108,
                111,
                6,
                168,
                31,
                134,
                164,
                136,
                72,
                98,
            ],
            29,
            98,
            80,
        )
    )
    # print(sln.minimumJumps([14, 4, 18, 1, 15], 3, 15, 9))
    # print(sln.minimumJumps([8, 3, 16, 6, 12, 20], 15, 13, 11))
    # print(sln.minimumJumps([1, 6, 2, 14, 5, 17, 4], 16, 9, 7))
