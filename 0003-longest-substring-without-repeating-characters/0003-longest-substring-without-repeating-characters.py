class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            # put charmap one-by-one 1) not appeared 2) appeared before the new start point
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            # next start point : right after the duplicated alphabet
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        
        return maxLength
        