class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp, score = 0, 0

        # (values[i] + i) + (values[j]-j): dp + (x-i)
        for i, x in enumerate(values):
            score = max(score, dp+x-i)
            dp = max(dp, x+i) # i increases, (values[i] + i) maximum
        return score



            
        