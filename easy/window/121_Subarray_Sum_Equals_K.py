'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for sell in prices:
            max_profit = max(max_profit, sell-min_buy)
            min_buy = min(min_buy, sell)
        return max_profit
assert Solution().maxProfit(prices = [10,1,5,6,7,1]) == 6