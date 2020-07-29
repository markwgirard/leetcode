class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, hold, sell, cool, nothing = float('-inf'), float('-inf'), float('-inf'), float('-inf'), 0
        for p in prices:
            buy, hold, sell, cool, nothing = max(cool, nothing) - p, max(buy, hold), max(buy, hold) + p, sell, max(cool, nothing)
        return max(buy, hold, sell, cool, nothing)
        
        
# Idea: Use DP to keep track of the most amount of money that could have been earned so far if, 
# on the current day, you either bought, held, sold, were cooling off, or doing nothing. 
#   - The only way you can buy today is if the previous day you did nothing or were cooling off. Take the max, then you spend p.
#   - The only way you can hold today is if the previous day you bought or were already holding. Take the max.
#   - The only way you can sell today is if the previous day you bought or were already holding. Take the max, then you earn p.
#   - The only way you can be cooling today is if the previous day you sold.
#   - The only way you can do nothing today is if the previous day you were cooling or doing nothing. Take the max.
