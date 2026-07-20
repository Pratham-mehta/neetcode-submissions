# Idea to solve this problem
# 1. Intialize left pointer and consider it as Buy Day 
# (Lower is Better); Put it to first index of List
# l = 0
# 2. Intialize right pointer and consider it as Sell Day
# (Higher is Better); Sell it on Next Day
# r = 1
# 3. Result variable to track the Profit made
# 4. Loop right pointer until we do not get the max price 
# 4.1 Or else move Left to Right (Since there is a cheap price found)
# 4.2 Increment R to the Next Day
# 5. Compute & return the result (max profit)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        maxP = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r+=1
        
        return maxP
    




