class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            check = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) <= i or strs[j][i] != check:
                    return ans
            ans += check
        
        return strs[0]

