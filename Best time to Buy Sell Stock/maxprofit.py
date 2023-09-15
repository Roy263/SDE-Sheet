class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit=0
        l=0
        r=1
        n=len(prices)
        while(r<n):
            print(f"l: {l} r: {r}")
            profit=prices[r]-prices[l]
            print(profit)
            if(prices[l]<prices[r]):
                maxprofit=max(profit,maxprofit)
            else:
                l=r
            r+=1
        return maxprofit

if __name__=="__main__":
    obj=Solution()
    arr=[7,1,5,3,6,4]
    print(obj.maxProfit(arr))