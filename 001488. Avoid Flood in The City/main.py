from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full = {}
        empty = []

        i = 0
        l = len(rains)
        ans = [-1] * l
        while i < l:
            if rains[i] > 0:
                prev = full.get(rains[i])
                if prev is not None:
                    if len(empty) == 0:
                        return []
                    
                    j = 0
                    found = False
                    while j < len(empty):
                        if empty[j] > prev:
                            found = True
                            break
                        j += 1

                    if not found:
                        return []

                    k = empty[j]
                    ans[k] = rains[i]
                    del full[rains[i]]
                    empty.remove(k)

                ans[i] = -1
                full[rains[i]] = i
            else:
                ans[i] = 1
                empty.append(i)
            # print(f"i={i}, full={full}, rain_i={rains[i]}, ans={ans}")
            i += 1
 
        return ans
                

if __name__ == "__main__":
    sln = Solution()
    print(sln.avoidFlood([1,0,2,3,0,1,2])) # [-1,1,-1,-1,2,-1,-1]
    print(sln.avoidFlood([1,0,2,0,2,1])) # [-1,1,-1,2,-1,-1]
    print(sln.avoidFlood([1,0,2,0])) # [-1,1,-1,1]
    print(sln.avoidFlood([0,1,1])) # []
    print(sln.avoidFlood([69,0,0,0,69])) # [-1, 69, 1, 1, -1]
    print(sln.avoidFlood([1,2,3,4]))  # [-1, -1, -1, -1]
    print(sln.avoidFlood([1,2,0,0,2,1])) # [-1, -1, 2, 1, -1, -1]
    print(sln.avoidFlood([1,2,0,1,2])) # []