class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            # bracket start point
            if s[i] == "(":
                stack.append(i)
            else:
                # bracket closed
                stack.pop()
                # maintain one ')' : beginning of complet bracket set 
                if len(stack) == 0:
                    stack.append(i)
                # no remaining open bracket
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
        