class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if numRows == 1:
        #     return s
        # rows = {}
        # for i in range(numRows):
        #     rows[i] = ""
        # row = 0
        # direction = 1
        # for i in range(len(s)):
        #     rows[row] += s[i]
        #     row += direction
        #     if row == numRows-1 or row == 0:
        #         direction *= -1
        # result = ""
        # for value in rows.values():
        #     result += value
        # return result

        if numRows == 1:
            return s
        rows = [''] * min(numRows, len(s))
        curRow, goingDown = 0, False

        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        return ''.join(rows)