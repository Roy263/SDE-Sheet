class Solution:
    def equalsum(self,arr):
        n=len(arr)-1
        for i in range(n):
            rsum=sum(arr[:i])
            lsum=sum(arr[i+1:])
            if(rsum==lsum):
                return i+1
        return -1

if __name__=='__main__':
    arr=[1,4,2,5]
    obj=Solution()
    print(obj.equalsum(arr))
