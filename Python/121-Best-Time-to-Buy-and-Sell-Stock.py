class Solution(object):
    def maxProfit(self, prices):
        minj=prices[0]
        maxs=0
        for i in prices:
            current=i
            if i<minj:
                minj=i
            profit=current-minj
            if maxs<profit:
                maxs=profit
        return maxs        


        