class Solution:
    def maxScore(self, s: str) -> int:
        right = s.count('0')
        ans, left = 0, 0
        for i in range(1, len(s)):
            if s[i - 1] == '0':
                left += 1
                right -= 1
            ans = max(ans, left + (len(s) - right - i))
        return ans