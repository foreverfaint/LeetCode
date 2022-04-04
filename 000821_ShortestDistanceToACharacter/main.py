from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = len(s)
        i = 0
        ans = [float("inf")] * l
        while i < l:
            if s[i] == c:
                j = i - 1
                k = 1
                while j >= 0:
                    if s[j] == c:
                        break
                    ans[j] = min(ans[j], k)
                    k += 1
                    j -= 1

                j = i + 1
                k = 1
                while j < l:
                    if s[j] == c:
                        break
                    ans[j] = k
                    k += 1
                    j += 1
                
                ans[i] = 0
            i += 1
        return ans




if __name__ == "__main__":
    sln = Solution()
    print(sln.shortestToChar(s = "loveleetcode", c = "e"))
    print(sln.shortestToChar(s = "aaab", c = "b"))