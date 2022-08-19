#You are given an array prices where prices[i] is the price of a
#given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy 
#one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. 
#If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l , r = 0 , 1
        maxP = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit,maxP)
            else:
                l=r
            r+=1
        return maxP
                
        
def main():
    prices = [7,1,5,3,6,4]
    res = Solution()
    ros = res.maxProfit(prices)
    print(ros)
if __name__ == "__main__":
    main()

