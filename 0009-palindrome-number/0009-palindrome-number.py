class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        str_int = str(x)
        for i in range(len(str_int)//2):
            if str_int[i] != str_int[-1-i]:
                return False

        return True
