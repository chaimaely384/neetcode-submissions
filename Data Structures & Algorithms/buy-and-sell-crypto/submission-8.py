class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        b, s = 0, 1
        profit = 0
        while s <len(prices):
            if prices[b]<prices[s]:
                profit = max(profit,(prices[s]-prices[b]))
                s = s+1
            else :
                b , s = s, s+1
        return profit
        

            
        