import time
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        flag=1
        k-=1
        print("k:",k)
        rowsize=2**(n-1)
        print(rowsize)
        left=0
        right=rowsize-1
        while left<right:
            mid=left+(right-left)//2
            print(f"left:{left} right:{right} mid:{mid}")
            time.sleep(2)
            
            if(k>mid):
                flag=0
                left=mid+1
            elif (k<=mid):
                right=mid
        return (flag+1)%2  
                

if __name__=="__main__":
    obj=Solution()
    n=4
    k=6
    result=obj.kthGrammar(n,k)
    print(result)