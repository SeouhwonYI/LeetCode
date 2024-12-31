class Solution:
    def romanToInt(self, s: str) -> int:
        # roman = {"I": 1, "V": 5, "X": 10, "L": 50,
        #          "C": 100, "D": 500, "M": 1000}
        # sol = 0
        # for i in range(len(s)):
        #     if i < len(s)-1 and roman[s[i]] < roman[s[i+1]]:
        #         sol -= roman[s[i]]
        #     else:
        #         sol += roman[s[i]]

        # return sol

        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number