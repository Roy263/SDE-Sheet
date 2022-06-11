class Solution:
    def sortColors(self,nums):
        n0=nums.count(0)
        n1=nums.count(1)
        n2=nums.count(2)
        nums=[0]*n0+[1]*n1+[2]*n2
        return nums
if __name__ == "__main__":
    print(Solution().sortColors([2,0,2,1,1,0]))