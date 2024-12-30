class Solution:
    def reverse(self, x: int) -> int:
        # abs_x = abs(x)
        # positive = (x == abs_x)
        # out = 0
        # while abs_x:
        #     out = out * 10 + abs_x % 10
        #     abs_x = abs_x // 10
        # result = out if positive else -out
        # if result < -2**31 or result >= 2**31:
        #     return 0
        # else: return result

        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        if res < -2**31 or res >= 2**31:
            return 0
        else: return res