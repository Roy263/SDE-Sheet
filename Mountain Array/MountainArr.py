def findmaxLinerarSearch(array):
    max=0
    for i in arr:
        if i>max:
            max=i
    return max

def findMaxBinarySearch(arr):
    n=len(arr)
    mid=int(n/2)
    if(n==2): 
        return arr[0] if arr[0]>arr[1] else arr[1]
    else:
        m=arr[mid]
        if(m>arr[mid-1] and m<arr[mid+1]):
            print("mid is peak")
            return m
        if(m>arr[mid-1] and arr[mid+1]>m):
            print("peak is on the right")
            return findmaxLinerarSearch(arr[mid:n-1])
        if(m<arr[mid-1] and m>arr[mid+1]):
            print("peak is on the left")
            return findmaxLinerarSearch(arr[:mid])
arr=[7,8,11,12,13,15,9,5,2]
print(findMaxBinarySearch(arr))