class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x<0: return False
        # str_int = str(x)
        # for i in range(len(str_int)//2):
        #     if str_int[i] != str_int[-1-i]:
        #         return False

        # return True

        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        original = x

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10