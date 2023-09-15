class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxsum(i):
          print(i)
          if(maxarr[i]!=None):
            return maxarr[i]
          maxarr[i]=max(nums[i],maxsum(i-1)+nums[i])
          print(maxarr)
          return maxarr[i]
        n=len(nums)
        maxarr=[None for _ in range(n)]
        maxarr[0]=nums[0]
        print(maxarr)
        maxsum(n-1)
        return max(maxarr)

if __name__=='__main__':
    obj=Solution()
    arr1=[-2,1,-3,4,-1,2,1,-5,4]
    print(obj.maxSubArray(arr1))