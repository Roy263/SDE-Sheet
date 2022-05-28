class Solution:	
	def binarysearch(self, arr, n, k):
		(l,r)=(0,n-1)
		while (l<=r):
		    mid=(l+r)//2
		    if k==arr[mid]:
		        return mid
		    elif(k<arr[mid]):
		        r=mid-1
		    else:
		        l=mid+1
		return -1

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split(' ')))
        k=int(input())
        obj=Solution()
        print(obj.binarysearch(arr,n,k))