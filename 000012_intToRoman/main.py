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
    def intToRoman(self, num: int) -> str:
        i = 1
        s = ""
        while num > 0:
            s = self.m[i * (num % 10)] + s
            num = num // 10
            i *= 10
        return s


if __name__ == "__main__":
    assert "III" == Solution().intToRoman(3)
    assert "L" == Solution().intToRoman(50)
    assert "LVIII" == Solution().intToRoman(58)
    assert "MCMXCIV" == Solution().intToRoman(1994)