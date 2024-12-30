class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        first = s[0]
        value = ""
        sign = True
        if first == "-":
            sign = False
        elif ord(first) >= 48 and ord(first) <= 57:
            value += first
        elif first != "+":
            return 0
        
        for c in s[1:]:
            if ord(c) >= 48 and ord(c) <= 57:
                value += c
            else:
                break

        if value:
            result = int(value) if sign else -int(value)
        else:
            return 0

        if result < -2**31:
            result = -2**31
        elif result >= 2**31:
            result = 2**31 - 1
        return result