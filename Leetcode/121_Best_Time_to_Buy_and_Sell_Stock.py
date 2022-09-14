'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to 
buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
'''
class Solution:
    def maxProfit(self ,prices):
        self.prices = prices
        
        
        
        if (max(self.prices) - min(self.prices)) > 0:
            return max(self.prices) - min(self.prices)
        else:
            return 0

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))


# a = [7,1,5,3,6,4]
# if 
# print(min(a),max(a))