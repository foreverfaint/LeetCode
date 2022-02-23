class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        curr_l = 0
        curr_r = ""
        curr_s = set()
        for c in s:
            if c not in curr_s:
                curr_r += c
                curr_l += 1
                curr_s.add(c)
            else:
                i = 0
                for c2 in curr_r:
                    if c2 != c:
                        i += 1
                        curr_l -= 1
                        curr_s.remove(c2)
                    else:
                        break
                curr_r = curr_r[i + 1:] + c
            
            if curr_l > max_l:
                max_l = curr_l
                
        return max_l
            

if __name__ == "__main__":
    assert 3 == Solution().lengthOfLongestSubstring("abcabcbb")
    assert 1 == Solution().lengthOfLongestSubstring("bbbbb")
    assert 3 == Solution().lengthOfLongestSubstring("pwwkew")