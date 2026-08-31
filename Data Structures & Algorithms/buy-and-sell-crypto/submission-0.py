class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, answer = 0,0,0
        sellValue, buyValue = 0,0
        for i in range(len(prices)):
            val = prices[i]
            if i == 0:
                buyValue, sellValue = val, val
                continue
            # check profit by taking right value - left value
            # if profit > answer -- update answer move right, if it is less, I will move left
            
            if val < buyValue:
                buyValue = val
                left = i
                if right < left:
                    right = i
                    sellValue = val
            elif val > sellValue:
                sellValue = val
                right = i
            profit = sellValue - buyValue
            answer = max(answer, profit)

        return answer