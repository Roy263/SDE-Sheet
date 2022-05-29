# Write a program to print all the LEADERS in the array.
# An element is leader if it is greater than all the elements to its right side. 
# And the rightmost element is always a leader. 

class Solution:
    def findleader(self,arr):
        leader=[]
        n=len(arr)
        for i in range(n-1):
            if arr[i]>max(arr[i+1:]):
                leader.append(arr[i])
        leader.append(arr[n-1])
        return leader

if __name__=='__main__':
    arr=[16,17,4,3,5,2]
    obj=Solution()
    print(obj.findleader(arr))