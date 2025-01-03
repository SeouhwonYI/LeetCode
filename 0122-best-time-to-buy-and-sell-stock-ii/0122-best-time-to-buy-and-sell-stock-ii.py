class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = prices[0]
        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] < buy:
        #         buy = prices[i]
        #     else: 
        #         profit += prices[i] - buy
        #         buy = prices[i]
        # return profit

        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit