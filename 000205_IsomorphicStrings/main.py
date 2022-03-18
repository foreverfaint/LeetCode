from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m_s2t = {}
        m_t2s = {}
        for i in range(len(s)):
            actual_c_s = s[i]
            actual_c_t = t[i]
            expected_c_s = m_t2s.get(actual_c_t)
            expected_c_t = m_s2t.get(actual_c_s)
            if not expected_c_s and not expected_c_t:
                m_t2s[actual_c_t] = actual_c_s
                m_s2t[actual_c_s] = actual_c_t
            elif expected_c_s and expected_c_t and expected_c_s == actual_c_s and expected_c_t == actual_c_t:
                continue
            else:
                return False
        return True
            


if __name__ == "__main__":
    sln = Solution()
    print(sln.isIsomorphic("badc", "baba"))
    print(sln.isIsomorphic("egg", "add"))
    print(sln.isIsomorphic("foo", "bar"))
    print(sln.isIsomorphic("paper", "title"))