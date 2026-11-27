from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cheapest_price = min(price for _, price in items)
        dp = [0] * (budget + 1)

        for factor, price in items:
            if price > budget:
                continue
            copies = sum(1 for other_factor, _ in items
                         if other_factor % factor == 0)

            for money in range(budget, price - 1, -1):
                dp[money] = max(dp[money], dp[money - price] + copies)

        return max(
            dp[money] + (budget - money) // cheapest_price
            for money in range(budget + 1)
        )