class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        l=0
        r=n-1
        i=0
        while(i<=r):
            if(nums[i]==0):
                t=nums[i]
                nums[i]=nums[l]
                nums[l]=t
                i+=1
                l+=1
            elif(nums[i]==2):
                t=nums[i]
                nums[i]=nums[r]
                nums[r]=t
                r-=1
            else:
                i+=1
        return nums
if __name__ == "__main__":
    print(Solution().sortColors([2,0,2,1,1,0]))