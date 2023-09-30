'''
given an array of integers find the max sum of the array by flipping the negative number to positive 
if there are cosecutive negative numbers then you can flip both the numbers together and add them to sum
''''


class Solution():
    def maxsum(self,arr):
        n=len(arr)
        neg_arr=[]
        sum=0
        for i in range(n):
            if(arr[i]<0):
                neg_arr.append((arr[i],i))
            else:
                sum+=arr[i]
        max_consecutive_sum=0
        current_consecutive_sum=0
        for ele,pos in neg_arr:
            print(ele,pos)
            if(current_consecutive_sum>0 and pos == prev_pos+1):
                current_consecutive_sum+=abs(ele)
            else:
                current_consecutive_sum=abs(ele)
            print("current neg",current_consecutive_sum)
            max_consecutive_sum=max(max_consecutive_sum,current_consecutive_sum)
            print("max of neg",max_consecutive_sum)
            prev_pos=pos
        return sum+max_consecutive_sum


if __name__=="__main__":
    obj=Solution()
    arr=[1,2,3,4,-5,-6,1,-8,10,-9,-1]
    print(obj.maxsum(arr))
    [2,3,-4,-5,6,7,-8,-9]