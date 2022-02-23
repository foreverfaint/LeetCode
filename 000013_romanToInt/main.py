class Solution:
    m = {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC",
        100: "C",
        200: "CC",
        300: "CCC",
        400: "CD",
        500: "D",
        600: "DC",
        700: "DCC",
        800: "DCCC",
        900: "CM",
        1000: "M",
        2000: "MM",
        3000: "MMM",
    }

    def romanToInt(self, s: str) -> int:
        m2 = {}
        for i, r in self.m.items():
            m2[r] = i

        r = 0
        while len(s) > 0:
            for l in range(4, 0, -1):
                p = m2.get(s[0:l])
                if p:
                    r += p
                    s = s[l:]
                    break
        return r



if __name__ == "__main__":
    assert 3 == Solution().romanToInt("III")
    assert 10 == Solution().romanToInt("X")
    assert 58 == Solution().romanToInt("LVIII")
    assert 1994 == Solution().romanToInt("MCMXCIV")