from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        days = len(pizzas) // 4
        odds = (days + 1) // 2
        odd_day_sum = sum(pizzas[:odds])
        evens = days // 2
        even_day_sum = sum(pizzas[odds + 1 : odds + evens * 2 : 2])
        return odd_day_sum + even_day_sum
