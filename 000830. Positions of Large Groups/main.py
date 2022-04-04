from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        groups = [[]]
        for i, c in enumerate(s):
            if not groups[-1]:
                groups[-1].append(i)
            elif s[groups[-1][-1]] == c:
                groups[-1].append(i)
            else:
                groups.append([])  
                groups[-1].append(i)

        groups = [[group[0], group[-1]] for group in groups if len(group) >= 3]
        return groups


if __name__ == "__main__":
    sln = Solution()
    print(sln.largeGroupPositions("abbxxxxzzy"))
    print(sln.largeGroupPositions("abc"))
    print(sln.largeGroupPositions("abcdddeeeeaabbbcd"))