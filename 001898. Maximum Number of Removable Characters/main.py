from typing import List


class Solution:
    def is_sub(self, s, p):
        i_s = 0
        i_p = 0
        l_s = len(s)
        l_p = len(p)
        if l_s < l_p:
            return False

        while i_p < l_p and i_s < l_s:
            if s[i_s] == p[i_p]:
                i_p += 1
            i_s += 1
        return i_p >= l_p

    def make_sub_1(self, s, removable):
        return "".join([c for i, c in enumerate(s) if i not in set(removable)])

    def make_sub_2(self, s, removable):
        ch_list = list(iter(s))
        for i in removable:
            ch_list[i] = ""
        return "".join(ch_list)

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        low = 0
        high = len(removable) + 1
        while low < high:
            k = (low + high) // 2
            sub_s = self.make_sub_2(s, removable[:k])
            is_sub = self.is_sub(sub_s, p)
            # print(low, k, high, sub_s, p, is_sub)
            if is_sub:
                low = k + 1
            else:
                high = k
        return low - 1



if __name__ == "__main__":
    sln = Solution()
    print(sln.maximumRemovals(s = "ab", p = "ab", removable = [0]))
    print(sln.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0]))
    print(sln.maximumRemovals(s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]))
    print(sln.maximumRemovals(s = "abcab", p = "abc", removable = [0,1,2,3,4]))