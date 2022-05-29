class Solution:
    def leaders(self, arr):
        n=len(arr)
        leaders=list()
        maxval = float('-inf')
        for i in reversed(range(0, n)):
            if arr[i]>=maxval:
                maxval = arr[i]
                leaders.append(maxval)
        return leaders