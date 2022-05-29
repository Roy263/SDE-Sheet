class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l=0
        r=len(arr)-1
        while(l<=r):
            m=(l+r)//2
            if(r==l+1) and arr[l]>=arr[r]:
                return l
            if(r==l+1) and arr[r]>=arr[l]:
                return r
            if arr[m]>arr[m+1] and arr[m]>arr[m-1]:
                return m
            if arr[m]>arr[m+1] and arr[m]<arr[m-1]:
                r=m-1
            else: 
                l=m+1
        return -1
if __name__=='__main__':
    obj=Solution()
    arr=[1,3,7,8,9,6,2,0]
    print(obj.peakIndexInMountainArray(arr))