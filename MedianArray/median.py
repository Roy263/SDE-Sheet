class Solution(object):
    def mergeArrays(self,arr1,arr2):
        arr=arr1+arr2
        arr=set(arr)
        return list(arr)
    def findMedian(self,arr,n):
        if(n%2==0):
            return (arr[n//2]+arr[(n-1)//2])/2
        else:
            return arr[n/2]
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr=self.mergeArrays(nums1,nums2)
        print("array ",arr)
        return self.findMedian(arr,len(arr))


if __name__=='__main__':
    obj=Solution()
    arr1=[1,2]
    arr2=[3]
    print(obj.findMedianSortedArrays(arr1,arr2))