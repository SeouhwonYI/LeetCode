class Solution:
    def longestPalindrome(self, s: str) -> str:
        # max_len = 1
        # max_str = s[0]
        # # define matrix
        # matrix = [[False for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s)):
        #     # each character itself 
        #     matrix[i][i] = True
        #     for j in range(i):
        #         # j = i & (1~3 letters or [j+1]~[i-1] is palindrome)
        #         if s[j] == s[i] and (i-j<=2 or matrix[j+1][i-1]):
        #             matrix[j][i] = True
        #             if i-j+1 > max_len:
        #                 max_len = i-j+1
        #                 max_str = s[j:i+1]
        # return max_str

        max_len=1
        max_str=s[0]
        # make # w # o # r # d # s #
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0

        for i in range(len(s)):
            # even i: 0 / odd i: use dp in leftside of palindrome
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])

            # outer side equal
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1

            # new palindrome -> change center and right
            if i+dp[i] > right:
                center = i
                right = i+dp[i]

            # longest palindrome
            if dp[i] > max_len:
                max_len = dp[i]
                max_str = s[i-dp[i]:i+dp[i]+1].replace('#','')
                
        return max_str
