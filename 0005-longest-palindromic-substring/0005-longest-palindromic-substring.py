class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_str = s[0]
        # define matrix
        matrix = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            # each character itself 
            matrix[i][i] = True
            for j in range(i):
                # j = i & (1~3 letters or [j+1]~[i-1] is palindrome)
                if s[j] == s[i] and (i-j<=2 or matrix[j+1][i-1]):
                    matrix[j][i] = True
                    if i-j+1 > max_len:
                        max_len = i-j+1
                        max_str = s[j:i+1]
        return max_str