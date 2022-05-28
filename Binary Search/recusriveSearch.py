class Solution:
    def binarySearch(self,arr,l,r,k):
        if l>r:
            return -1
        mid=(l+r)//2
        if(k==arr[mid]):
            return mid
        elif(k<arr[mid]):
            return self.binarySearch(arr,l,mid-1,k)
        else:
            return self.binarySearch(arr,mid+1,r,k)

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split(' ')))
        k=int(input())
        obj=Solution()
        print(obj.binarySearch(arr,0,n-1,k))