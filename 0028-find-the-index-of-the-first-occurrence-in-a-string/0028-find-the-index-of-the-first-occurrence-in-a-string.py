class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            idx = 0
            while haystack[i+idx] == needle[idx]:
                idx += 1
                if idx == len(needle):
                    return i
        
        return -1