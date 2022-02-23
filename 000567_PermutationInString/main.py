from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False

        def _hm(lst, i, n):
            m = {}
            while i < n:
                m.setdefault(lst[i], 0)
                m[lst[i]] += 1
                i += 1
            return m

        def _cmp(hm1, hm2):
            if len(hm1) != len(hm2):
                return False

            for k1, v1 in hm1.items():
                v2 = hm2.get(k1)
                if v2 != v1:
                    return False

            for k1, v1 in hm2.items():
                v2 = hm1.get(k1)
                if v2 != v1:
                    return False

            return True

        def _del(hm, c):
            v = hm.get(c)
            if v:
                hm[c] = v - 1
                if v == 1:
                    del hm[c]

        def _add(hm, c):
            hm.setdefault(c, 0)
            hm[c] += 1
 
        s1 = list(iter(s1))
        hm_s1 = _hm(s1, 0, l1)
        s2 = list(iter(s2))
        hm_s2 = _hm(s2, 0, l1)
        i = 0
        while True:
            if _cmp(hm_s1, hm_s2):
                return True

            _del(hm_s2, s2[i])
            
            i += 1
            if i + l1 > l2:
                return False

            _add(hm_s2, s2[i + l1 - 1])


if __name__ == "__main__":
    sln = Solution()

    print(sln.checkInclusion("ab", "ba"))
    print(sln.checkInclusion("abc", "abacd"))
    print(sln.checkInclusion("ab", "eidbaooo"))
    print(sln.checkInclusion("ab", "eidboaoo"))