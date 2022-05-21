def twosum(nums,target):
    s={}
    for i in range(len(nums)):
        diff=target-nums[i]
        if(diff in s):
            return [i,s[diff]]
        s[nums[i]]=i

arr=[2,7,11,15]
target=9
print(twosum(arr,target))