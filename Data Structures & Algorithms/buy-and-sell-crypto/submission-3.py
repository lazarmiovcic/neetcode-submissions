class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the price on r is less on l so we just set l to r, there is no point in iterating l since r is already used for exploration. So there are 2 rules: 1) if the new profit is greater than maxp, maxp = current profit; 2) if current profit < 0 then we found a price that is less than our current buying price, so we can set l to r.
        l, r = 0, 1
        buy, sell = 0, 0
        maxp = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            else:
                maxp = max(maxp, profit)
            r+=1
        return maxp
             

