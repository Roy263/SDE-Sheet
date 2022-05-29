class Solution:
    def findMax(self,arr,l,h):
        if l==h:
            return arr[l]
        if h==l+1 and arr[l]>=arr[h]:
            return arr[l]
        if h==l+1 and arr[h]>=arr[l]:
            return arr[h]
        mid=(l+h)//2
        if(arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]):
            return arr[mid]
        elif(arr[mid]>arr[mid+1] and arr[mid]<arr[mid-1]):
            return self.findMax(arr,l,mid-1)
        else:
            return self.findMax(arr,mid+1,h)
        
if __name__=='__main__':
    obj=Solution()
    arr=[1,3,7,8,9,6,2,0]
    print(obj.findMax(arr,0,len(arr)-1))