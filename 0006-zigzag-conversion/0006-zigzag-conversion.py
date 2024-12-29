class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = {}
        for i in range(numRows):
            rows[i] = ""
        row = 0
        direction = 1
        for i in range(len(s)):
            rows[row] += s[i]
            row += direction
            if row == numRows-1 or row == 0:
                direction *= -1
        result = ""
        for value in rows.values():
            result += value
        return result
