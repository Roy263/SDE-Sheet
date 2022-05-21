def findmax(arr):
    max=0
    for i in arr:
        if i>max:
            max=i
    return max
arr=[7,8,13,15,17,12,9,5,2]
print(findmax(arr))