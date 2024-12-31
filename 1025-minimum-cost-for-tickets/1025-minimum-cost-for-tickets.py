class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last7 = []
        last30 = []
        cost = 0

        for d in days:
            # invalid 7-day pass on day d
            while last7 and last7[0][0] + 7 <= d:
                last7.pop(0)
            # invalid 30-day pass on day d    
            while last30 and last30[0][0] + 30 <= d:
                last30.pop(0)
            # after above, it remains valid cases on day d
            
            last7.append((d, cost + costs[1]))
            last30.append((d, cost + costs[2]))
            # one-day pass? or 7-day or 30-day pass?
            cost = min(cost + costs[0], last7[0][1], last30[0][1])

        return cost