class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = int(1e9 + 7)
        dp = [0] * (high + 1)
        # base case: "" (one way to create empty string)
        dp[0] = 1

        for i in range(high+1):
            # If lenghth-i string is possible 
            if dp[i] > 0:
                # putting zero is also possible
                if i + zero <= high:
                    # i+zero itself / or / (i) + (zero * "0")
                    dp[i+zero] = (dp[i+zero] + dp[i]) % mod
                if i + one <= high:
                    dp[i+one] = (dp[i+one] + dp[i]) % mod
        
        result = 0
        for i in range(low, high+1):
            result = (result + dp[i]) % mod
        return result