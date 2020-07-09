class Solution(object):
    def maxProfit(self, prices):
        profit=0
        k=len(prices)
        for i in range (1,k):
            profit+=max(prices[i]-prices[i-1],0)
        print("\n"+str(profit))
        return profit
z=Solution()
s=[1,2,3,2,7,10,5,9,7,6,2,5]
z.maxProfit(s)