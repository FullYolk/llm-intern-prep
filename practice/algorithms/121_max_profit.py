from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = -float('inf')
        for i in prices:
            if i < min_price:
                min_price = i
            if i - min_price > max_profit:
                max_profit = i - min_price
        return max_profit